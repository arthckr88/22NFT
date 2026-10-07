# QA / retries / validation record

- Native Py 3.14 cannot install bpy because external DNS is restricted. Retried using installed Blender 5.2.2 LTS.
- Headless Blender Metal detection crashed on a nil device name. Local ad-hoc copied executable + null-safe strstr interpose enabled CPU Blender; installed app unchanged.
- First model build hit renamed Sky Texture enum in Blender 5.2. Retried with MULTIPLE_SCATTERING (current physical sky API).
- Initial exterior inspection caught invalid sidewall/cab/car boolean shading. Corrected primitive normals, applied bevels before booleans, used round wheel openings and rerendered. Final exterior no longer contains diagonal wall artifacts.
- Tail cutaway inspection exposed washer B in the framing and a stacked-pack/frame interference. Hid unrelated appliance layers, rearranged packs side by side, lowered the enclosure lid below the reconstructed rail and revised the envelope to 45.5 × 37 × 9.5 in. Geometry envelope remains ESTIMATE, cooling/service margins unverified.
- Ghosted power view opened the tail enclosure for component visibility; thin ghosted outline retained. Colored conductors are topology only.
- First Three.js bundle failed due unresolved bare module imports. Retried with a local esbuild alias. Vendored Three.js 0.169.0 and official Jost / IBM Plex Mono fonts avoid CDN dependencies.
- Direct view_image and computer-use services timed out/closed. Retried with local JPEG image bytes emitted in the tool result; visual inspection succeeded.
- All final renders: native CPU Cycles, 1920 × 1080, denoised, 24 exterior/technical and 32 interior/night samples. No generated-image substitutions.

Further completed-view checks and browser/PDF validation are recorded below as the deliverable is assembled.

- Browser automation: localhost DevTools connection rejected (EPERM). Retried Chrome with a direct debugging pipe and then a single-process software configuration; both exited before initialization. Interactive viewer therefore receives structural/logic validation here, not a claimed live-browser interaction pass. Native CoreText/CoreGraphics PDF fallback preserves searchable vector text, fonts and source links.
- Interior wide was rerendered with darker charcoal surfaces, richer oak, reduced exposure and a cab-view angle that reveals the retained rear desk. No geometry intersections visible in the final wide view.

- PDF verification helper initially hit an unwritable system Swift module cache. Retried with .runtime/swift-cache inside the workspace; compilation succeeded.

- Large PNG upload preparation exceeded cumulative execution output limits. Retried with small byte-range transfers and Git blob hash checks; native render files remained intact.
- Shared production layer behavior, actual GLTFLoader parsing of all 1,467 meshes, gzip model identity, published component envelopes and axle conservation passed Node validation. Live browser visual validation remains blocked.

- Final model revision: connected thin formed enclosure mounts, recessed pack handles, corrected washer envelope and provisional rear dual wheels. Views 01–11 were rerendered and individually inspected; no visible intersections or boolean wall artifacts remain.

- First night exterior showed a finite-ground/sky horizon stripe and a dull gray lighting balance. Extended the night floor, changed to a cool moonlit background/fill, kept warm window light and rerendered before acceptance.
- Elevation dimension labels overlapped in annotation review; separated their baselines. Added contrast behind the alternate A footprint and explicit Orion/generator floorplan callouts.
- Checkpoint patch rejected duplicate delete/add targets; rewrote the checkpoint directly and verified its file count.

- Night rerender accepted after individual inspection. All twelve final native frames are 1920 × 1080 and retained with source annotation anchors.
- The 51-page print book initially passed text clipping checks. All pages are rasterized for visual review; source-linked vector text and fonts are preserved. First 16 pages passed visual layout inspection.
- Full-array solar-harvest estimates now explicitly depend on an approved input arrangement; the single-input 50 A ×21.29 V ≈1.06 kW ceiling is recorded without inventing a clipped irradiance curve.

- Viewer power/tail presets now open enclosure walls/lid and hide cabin layers; exterior restores them. A case checkbox exposes internal hardware independently. A patch transport closure during validation editing was retried with small local Python edits, then rebundled.

- A fresh computer-use connection retry remained Transport closed. Live browser QA is still explicitly unverified. Actual power/exterior presets, the case toggle, case-node presence and embedded HTML control binding passed the shared-code Node checks.

- PDF spec-cell line breaks were restored after visual review (dimensions, mass and source notes now separated); repeated blank breaks collapse to a single line. Laundry wording was changed from surveyed to proposed to reflect the unmeasured production unit.

- FINAL: All twelve native frames and eight technical annotations are 1920 ×1080. Every render was visually inspected. All 51 PDF pages were visually reviewed, with refined specification and checklist pages checked again after line-break correction. Native PDF author reports zero clipped text.
- FINAL: Actual GLTFLoader parses 1,467 meshes; all eight layers, exclusive laundry behavior, power/exterior/case controls, embedded gzip identity, exported component envelopes and axle conservation pass. Browser inspection remains blocked, explicitly recorded rather than claimed passed.

- Direct report publication failed during host blob upload to chatgpt.com after a 300-second route timeout. Retrying the PDF alone, retaining the full-quality files and complete GitHub delivery path.

- PDF-only publication retry also timed out after 300 seconds at the host file-blob route. Direct artifact retention is unavailable in this session; complete files are supplied locally and committed to the requested GitHub branch for durable delivery.

- Later file transfers encountered intermittent exec-server disconnections and one truncated range. Retried with 49 KiB byte ranges, two readers and transport retries, preserving original files and checking Git blob hashes.
