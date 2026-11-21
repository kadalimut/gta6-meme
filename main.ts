// Entry for make.fun bounty gta6-meme-x-01: "Post a GTA 6 meme on X".
// The post itself is the entry. This program does one job only: it
// copies POST.json from the repository root into the output folder,
// where the gate reads the X post address from it. The house then
// reads the post (its first picture and its text) from X and hands
// that to the judge. Nothing written here is judged.
//
// Run it locally like this:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// out/POST.json is then byte for byte this directory's POST.json.

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(botDir, "POST.json");
if (!existsSync(source)) {
  console.error(`POST.json not found in ${botDir}`);
  process.exit(1);
}
mkdirSync(outputDir, { recursive: true });
copyFileSync(source, join(outputDir, "POST.json"));
console.log("POST.json copied to", outputDir);
