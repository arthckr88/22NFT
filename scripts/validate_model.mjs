import fs from 'node:fs';import crypto from 'node:crypto';
import {GLTFLoader} from '../book/vendor/examples/jsm/loaders/GLTFLoader.js';
import {Box3,Vector3} from '../book/vendor/build/three.module.js';
import {setLayer,setServiceCase,applyViewPreset} from './layers.js';
import {fileURLToPath} from 'node:url';
const R=fileURLToPath(new URL('../',import.meta.url));
globalThis.self=globalThis;
const raw=fs.readFileSync(R+'model/Alita-22NFT.glb');const buf=raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.byteLength);
if(raw.toString('utf8',0,4)!=='glTF'||raw.readUInt32LE(4)!==2||raw.readUInt32LE(8)!==raw.length)throw Error('GLB header invalid');
const parsed=JSON.parse(raw.subarray(20,20+raw.readUInt32LE(12)).toString());
const g=await new Promise((resolve,reject)=>new GLTFLoader().parse(buf,'',resolve,reject));const layers={};let meshes=0;g.scene.traverse(o=>{if(o.name.startsWith('LAYER_'))layers[o.name.slice(6)]=o;if(o.isMesh)meshes++;});
const expected=['shell','power','solar','laundry_A','laundry_B','interior','chassis','tow_car'];for(const n of expected)if(!layers[n])throw Error('Missing layer '+n);
let r=setLayer(layers,'laundry_A',true);if(!r.A||r.B)throw Error('A exclusivity');r=setLayer(layers,'laundry_B',true);if(r.A||!r.B)throw Error('B exclusivity');setLayer(layers,'shell',false);if(layers.shell.visible)throw Error('Shell toggle');setLayer(layers,'shell',true);
const checks=[];const normalize=s=>s.replace(/[^a-z0-9]/gi,'').toLowerCase();
const caseObjects=[];g.scene.traverse(o=>{if(['tailweatherenclosureestimate','removablegasketedenclosurelidestimate'].includes(normalize(o.name)))caseObjects.push(o);});
if(caseObjects.length!==2)throw Error('Missing service-case nodes');
applyViewPreset(layers,'power',caseObjects);if(layers.shell.visible||layers.interior.visible||caseObjects.some(o=>o.visible))throw Error('Power preset');
applyViewPreset(layers,'exterior',caseObjects);if(!layers.shell.visible||!layers.interior.visible||caseObjects.some(o=>!o.visible))throw Error('Exterior restore');
setServiceCase(caseObjects,false);if(caseObjects.some(o=>o.visible))throw Error('Case toggle');setServiceCase(caseObjects,true);

for(const [prefix,target] of [['Panel 1 275W aluminum frame',[.766064,.035052,1.73609]],['B4810 5.12kWh pack 1',[.608,.145,.38]],['RV5 hub 48V inverter',[.450088,.1599,.500126]],['A washer cabinet',[.5969,.847725,.55245]]]){
 let obj;g.scene.traverse(o=>{if(normalize(o.name)===normalize(prefix))obj=o;});if(!obj)throw Error('Missing component '+prefix);
 const sz=new Box3().setFromObject(obj).getSize(new Vector3());const got=[sz.x,sz.y,sz.z];if(got.some((v,i)=>Math.abs(v-target[i])>.0002))throw Error('Envelope mismatch '+prefix+' '+got);
 checks.push({component:prefix,exported_m:got,source_envelope_m:target,result:'PASS'});
}
const bounds=new Box3().setFromObject(g.scene);const size=bounds.getSize(new Vector3());
const html=fs.readFileSync(R+'book/Alita-22NFT-Interactive-Build-Book.html','utf8');if(!html.includes('data-case'))throw Error('Missing case control');const model64=html.match(/<script id="modeldata"[^>]*>([^<]+)<\/script>/)[1];const compressed=Uint8Array.from(Buffer.from(model64,'base64'));
const decomp=await new Response(new Blob([compressed]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();const hash=b=>crypto.createHash('sha256').update(Buffer.from(b)).digest('hex');if(hash(decomp)!==hash(raw))throw Error('Embedded model mismatch');
const a=JSON.parse(fs.readFileSync(R+'docs/analysis.json'));if(Math.abs(a.tail.front_lb+a.tail.rear_lb-a.tail.mass_lb)>.02)throw Error('Tail load sum');for(const v of Object.values(a.gross_totals))if(Math.abs(v.front_lb+v.rear_lb-v.gross_addition_lb)>.02)throw Error('Gross load sum');
const result={glbBytes:raw.length,sha256:hash(raw),parsedMeshes:meshes,layers:Object.keys(layers),layerToggleTests:'PASS (actual shared production function)',viewPresetTests:'PASS: power cutaway, exterior restoration, case toggle',embeddedGzipModel:'PASS using DecompressionStream API',axleConservation:'PASS',sceneBounds_m:{x:size.x,y:size.y,z:size.z},checks,browserVisualValidation:'BLOCKED: native browser automation exited; no live-browser pass claimed'};fs.writeFileSync(R+'docs/model-validation.json',JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
