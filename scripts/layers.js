// Shared layer behavior: actual viewer code and Node validation use this function.
export function setLayer(layers,key,on){
 if(layers[key])layers[key].visible=on;
 if(on&&key==='laundry_A'&&layers.laundry_B)layers.laundry_B.visible=false;
 if(on&&key==='laundry_B'&&layers.laundry_A)layers.laundry_A.visible=false;
 return {A:layers.laundry_A?.visible,B:layers.laundry_B?.visible};
}
export function setServiceCase(objects,on){for(const o of objects)o.visible=on;}
export function applyViewPreset(layers,key,caseObjects){
 if(key==='power'||key==='rear'){
  for(const name of ['shell','interior','laundry_A','laundry_B'])if(layers[name])layers[name].visible=false;
  if(layers.power)layers.power.visible=true;setServiceCase(caseObjects,false);
 }else if(key==='exterior'||key==='roof'){
  for(const name of ['shell','interior','power','solar'])if(layers[name])layers[name].visible=true;
  if(!layers.laundry_A?.visible&&!layers.laundry_B?.visible)setLayer(layers,'laundry_B',true);
  setServiceCase(caseObjects,true);
 }else if(key==='interior'){
  if(layers.shell)layers.shell.visible=false;if(layers.interior)layers.interior.visible=true;
  if(!layers.laundry_A?.visible&&!layers.laundry_B?.visible)setLayer(layers,'laundry_B',true);
 }
}
