# Before/After comparison (20 held-out prompts)

| Metric | Base | Fine-tuned |
|---|---|---|
| Valid Conventional Commit format | 0% | 95% |
| Commit type matches reference | 0% | 70% |
| Single-line output | 45% | 100% |


---

## Example 1
```diff
Write a Conventional Commit message for this diff:

diff --git a/playground/assets-sanitize/__tests__/assets-sanitize.spec.ts b/playground/assets-sanitize/__tests__/assets-sanitize.spec.ts
index c95cbf6d..2cb00f7f 100644
--- a/playground/assets-sanitize/__tests__/assets-sanitize.spec.ts
+++ b/playground/assets-sanitize/__tests__/assets-sanitize.spec.ts
@@ -1,10 +1,3 @@
 import { expect, test } fro
...
```
- **Reference:** `test(bundled-dev): enable fs-serve, resolve, dynamic-import and assets-sanitize cases (#23246)`
- **Base:** "```javascript\nfix(bundledDev ? 'denied .env' : 'denied .env', async () => {\n  expect(await page.textContent('.unsafe-dotenv')).toBe('403');\n})\n```"
- **Fine-tuned:** 'fix(playground): handle .env/.dotenv double slash (#14355)'

## Example 2
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/runtime-core/__tests__/componentEmits.spec.ts b/packages/runtime-core/__tests__/componentEmits.spec.ts
index 1b8bcf9a..e2540615 100644
--- a/packages/runtime-core/__tests__/componentEmits.spec.ts
+++ b/packages/runtime-core/__tests__/componentEmits.spec.ts
@@ -511,2 +511,3 @@ describe('component: emit', () => {
       FooBaz
...
```
- **Reference:** `fix(runtime-core): preserve once event listener name (#8341)`
- **Base:** "```conventional-commit\nisEmitListener(options, 'onOnce') // preserve event name `once`\n\nisEmitListener(options, 'onOnceOnce') // preserve event name `once` with `.once` modifier\n\nisEmitListener(options, 'onFooBaz') // preserve"
- **Fine-tuned:** 'fix(runtime-core): preserve event name when emitting listener (#14745)'

## Example 3
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/compiler-sfc/__tests__/templateTransformAssetUrl.spec.ts b/packages/compiler-sfc/__tests__/templateTransformAssetUrl.spec.ts
index cd14f105..82984ad6 100644
--- a/packages/compiler-sfc/__tests__/templateTransformAssetUrl.spec.ts
+++ b/packages/compiler-sfc/__tests__/templateTransformAssetUrl.spec.ts
@@ -152,2 +152,25 @@ desc
...
```
- **Reference:** `fix(compiler-sfc): preserve hash hrefs on `<image>` elements (#14756)`
- **Base:** 'The following Conventional Commit message fits the given diff:\n```typescript\n-  test(\'should not transform hash fragments on <image>\', () => {\n+  test(\'should not transform hash fragments on <image>\', () => {\n    // `<image href="#...">` is an in-document fragment'
- **Fine-tuned:** 'fix(compiler-sfc): avoid transforming hash fragments (#13745)'

## Example 4
```diff
Write a Conventional Commit message for this diff:

diff --git a/package.json b/package.json
index da9981b1..3948597c 100644
--- a/package.json
+++ b/package.json
@@ -3,3 +3,3 @@
   "version": "3.5.33",
-  "packageManager": "pnpm@10.33.0",
+  "packageManager": "pnpm@10.33.3",
   "type": "module",
...
```
- **Reference:** `chore(deps): update pnpm to v10.33.3 (#14760)`
- **Base:** 'Upgrade to PNP version 10.33.3'
- **Fine-tuned:** 'chore(deps): update pnpm to v10.33.3 (#15255)'

## Example 5
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/optimizer/index.ts b/packages/vite/src/node/optimizer/index.ts
index 1ab4291b..92968386 100644
--- a/packages/vite/src/node/optimizer/index.ts
+++ b/packages/vite/src/node/optimizer/index.ts
@@ -835,3 +835,3 @@ async function prepareRolldownOptimizerRun(
   if (external.length) {
-    plugins.push(rolldownCjsEx
...
```
- **Reference:** `fix(optimizer): preserve excluded optional peer require fallbacks (#23600)`
- **Base:** '* @param external The external dependencies to be rolled down.\n  * @param platform The platform of the project.\n  * @param environment The environment of the project.'
- **Fine-tuned:** 'fix(optimizer): handle external plugin in rollup (#23455)'

## Example 6
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/server/middlewares/transform.ts b/packages/vite/src/node/server/middlewares/transform.ts
index 10ee08d5..e3ff4628 100644
--- a/packages/vite/src/node/server/middlewares/transform.ts
+++ b/packages/vite/src/node/server/middlewares/transform.ts
@@ -58,2 +58,3 @@ const inlineRE = /[?&]inline\b/
 const svgRE = /\.s
...
```
- **Reference:** `fix(server): check `fs.serve` for `?vite-wasm-instance` (#23655)`
- **Base:** 'Deny `.env` file with `vite-wasm-instance` query'
- **Fine-tuned:** 'fix(fs-serve): prevent unsafe fetch from serving files with vite wasm instance (#23455)'

## Example 7
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/runtime-core/__tests__/components/Suspense.spec.ts b/packages/runtime-core/__tests__/components/Suspense.spec.ts
index 4abab7c5..319575b3 100644
--- a/packages/runtime-core/__tests__/components/Suspense.spec.ts
+++ b/packages/runtime-core/__tests__/components/Suspense.spec.ts
@@ -2478,2 +2478,96 @@ describe('Suspense', () =>
...
```
- **Reference:** `fix(teleport): handle updates before deferred mount (#14642)`
- **Base:** '```javascript\nshould not mount discarded teleport after suspense is resolved\n```'
- **Fine-tuned:** 'fix(runtime-core): avoid mounting teleport when suspense is resolved (#14559)'

## Example 8
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/runtime-dom/src/components/TransitionGroup.ts b/packages/runtime-dom/src/components/TransitionGroup.ts
index f8a0b471..af35e4bb 100644
--- a/packages/runtime-dom/src/components/TransitionGroup.ts
+++ b/packages/runtime-dom/src/components/TransitionGroup.ts
@@ -11,2 +11,3 @@ import {
 } from './Transition'
+import { type VSho
...
```
- **Reference:** `fix(transition): avoid move transition for hidden v-show group children (#14895)`
- **Base:** 'The commit message is already concise and informative. No changes were made in this diff.'
- **Fine-tuned:** 'fix(transition-group): avoid hidden v-show nodes from moving during transition (#14345)'

## Example 9
```diff
Write a Conventional Commit message for this diff:

diff --git a/package.json b/package.json
index 12d6e36d..60a5773d 100644
--- a/package.json
+++ b/package.json
@@ -49,3 +49,2 @@
     "@types/convert-source-map": "^2.0.3",
-    "@types/cross-spawn": "^6.0.6",
     "@types/etag": "^1.8.4",
diff --git a/packages/vite/LICENSE.md b/packages/vite/LICENSE.md
index 6d24a5e9..07a9200a 100644
--- a/packa
...
```
- **Reference:** `refactor: use `tinyexec` instead of `cross-spawn` (#23583)`
- **Base:** 'Add a Conventional Commit message for this diff:\n\n"Fix typo in package.json: update cross-spawn version"'
- **Fine-tuned:** 'chore(deps): update dependencies (#14355)'

## Example 10
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/plugins/importAnalysisBuild.ts b/packages/vite/src/node/plugins/importAnalysisBuild.ts
index d93f1919..ca10f62c 100644
--- a/packages/vite/src/node/plugins/importAnalysisBuild.ts
+++ b/packages/vite/src/node/plugins/importAnalysisBuild.ts
@@ -159,41 +159,44 @@ function preload(
     promise = allSettled(
-     
...
```
- **Reference:** `feat(build): avoid settling seen preload dependencies for performance (#23446)`
- **Base:** '```conventional-commit\npreload(\n  dependencies: [\n    "https://cdn.jsdelivr.net/npm/@vitejs/plugin-import@latest/dist/index.js",\n    "https://cdn.jsdelivr.net/npm/@vitejs/plugin-import@latest/dist/webpack-hot-middleware/bundle.js"\n  ],'
- **Fine-tuned:** 'fix(import-analysis): avoid importing assets URLs (#23875)'

## Example 11
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages-private/dts-test/ref.test-d.ts b/packages-private/dts-test/ref.test-d.ts
index 5d501464..9b6f699b 100644
--- a/packages-private/dts-test/ref.test-d.ts
+++ b/packages-private/dts-test/ref.test-d.ts
@@ -10,2 +10,3 @@ import {
   computed,
+  customRef,
   isRef,
@@ -550 +551,20 @@ const tRef2 = useTemplateRef<HTMLElement>('bar
...
```
- **Reference:** `fix(types): allow customRef to have different getter/setter types (#14639)`
- **Base:** '#14637 customRef with different getter/setter types'
- **Fine-tuned:** 'ref: fix custom ref with different getter/setter types (#14638)'

## Example 12
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/client/bundledDevClient.ts b/packages/vite/src/client/bundledDevClient.ts
index 416fe1a8..58de0bc2 100644
--- a/packages/vite/src/client/bundledDevClient.ts
+++ b/packages/vite/src/client/bundledDevClient.ts
@@ -26,2 +26,10 @@ if (typeof DevRuntime !== 'undefined') {
   class ViteDevRuntime extends DevRuntime {
+   
...
```
- **Reference:** `fix(bundled-dev): mark payload delivered on client report (#23373)`
- **Base:** "```javascript\nConventional Commit message (type(scope): summary). Output only the message:\n```javascript\nthis.environment.hot.on('vite:bundled-dev:payload-delivered', (payload) => {\n \tthis.markPayloadDelivered(payload.filename);\n});\n```\n\nThis is a conventional commit message"
- **Fine-tuned:** 'fix(bundled-dev): handle custom payload delivery (#15745)'

## Example 13
```diff
Write a Conventional Commit message for this diff:

diff --git a/pnpm-workspace.yaml b/pnpm-workspace.yaml
index 74ec7185..e71182b3 100644
--- a/pnpm-workspace.yaml
+++ b/pnpm-workspace.yaml
@@ -33 +33,3 @@ peerDependencyRules:
 minimumReleaseAge: 1440
+
+trustPolicy: no-downgrade
...
```
- **Reference:** `chore: enable pnpm trustPolicy: no-downgrade (#15330)`
- **Base:** 'no-downgrade'
- **Fine-tuned:** 'chore(deps): update peerDependencies (#14945)'

## Example 14
```diff
Write a Conventional Commit message for this diff:

diff --git a/playground/css/main.js b/playground/css/main.js
index 17d60741..f2788205 100644
--- a/playground/css/main.js
+++ b/playground/css/main.js
@@ -59,3 +59,2 @@ import './glob-dep.css'
 
-// eslint-disable-next-line import-x/order
 import { barModuleClasses } from '@vitejs/test-css-js-dep'
...
```
- **Reference:** `chore: remove eslint comment (#23325)`
- **Base:** 'A conventional commit message:\n"Fix import order in main.js file."'
- **Fine-tuned:** 'fix(playground): avoid importing `import` in CSS module (#23351)'

## Example 15
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/plugins/asset.ts b/packages/vite/src/node/plugins/asset.ts
index b7a0a1b3..05824909 100644
--- a/packages/vite/src/node/plugins/asset.ts
+++ b/packages/vite/src/node/plugins/asset.ts
@@ -47,3 +47,3 @@ import { getImportMapFilename } from './html'
 // referenceId is base64url but replaces - with $
-export const 
...
```
- **Reference:** `refactor: exclude postfix from `__VITE_ASSET__` (#22886)`
- **Base:** '* refactor: remove unused variable `match`.'
- **Fine-tuned:** 'refactor: remove unnecessary regex in asset (#23451)'

## Example 16
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/ssr/__tests__/ssrTransform.spec.ts b/packages/vite/src/node/ssr/__tests__/ssrTransform.spec.ts
index 59c45c93..7b91e6d4 100644
--- a/packages/vite/src/node/ssr/__tests__/ssrTransform.spec.ts
+++ b/packages/vite/src/node/ssr/__tests__/ssrTransform.spec.ts
@@ -779,2 +779,59 @@ function c({ _ = bar() + foo() }) {}
...
```
- **Reference:** `fix(ssr): rewrite computed key of destructing parameter (#23307)`
- **Base:** '#23232: Function argument destructure with a default parameter'
- **Fine-tuned:** 'fix(ssr): handle default parameters in function arguments (#23232)'

## Example 17
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages-private/sfc-playground/src/App.vue b/packages-private/sfc-playground/src/App.vue
index 7020211f..5a87a1d1 100644
--- a/packages-private/sfc-playground/src/App.vue
+++ b/packages-private/sfc-playground/src/App.vue
@@ -16,2 +16,4 @@ const useSSRMode = ref(false)
 
+const DEFAULT_TYPESCRIPT_VERSION = '6.0.3'
+
 const AUTO_SAVE_
...
```
- **Reference:** `chore(playground): default to TypeScript 6 (#15219)`
- **Base:** 'A conventional commit message:\nfeat(sfc-playground): update TypeScript version and auto save storage key'
- **Fine-tuned:** 'fix(sfc-playground): update default typescript version (#14955)'

## Example 18
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/vite/src/node/optimizer/scan.ts b/packages/vite/src/node/optimizer/scan.ts
index ca3f5fe5..62e9400f 100644
--- a/packages/vite/src/node/optimizer/scan.ts
+++ b/packages/vite/src/node/optimizer/scan.ts
@@ -613,10 +613,10 @@ function rolldownScanPlugin(
           if (
-            isInNodeModules(resolved) &&
-            isO
...
```
- **Reference:** `fix(optimizer): scan deep imports with custom extensions (#23678)`
- **Base:** 'discard unused dependencies during dep scan'
- **Fine-tuned:** 'fix(deps): skip scanning of dependencies in node_modules (#23451)'

## Example 19
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages/server-renderer/__tests__/ssrTeleport.spec.ts b/packages/server-renderer/__tests__/ssrTeleport.spec.ts
index 78c56942..27f78462 100644
--- a/packages/server-renderer/__tests__/ssrTeleport.spec.ts
+++ b/packages/server-renderer/__tests__/ssrTeleport.spec.ts
@@ -1,2 +1,2 @@
-import { Teleport, createApp, h } from 'vue'
+import
...
```
- **Reference:** `fix(ssr): resolve nested async teleport content (#9431)`
- **Base:** 'upgrade Vue version to v3'
- **Fine-tuned:** 'fix(server-renderer): resolve nested async content in teleport (#15341)'

## Example 20
```diff
Write a Conventional Commit message for this diff:

diff --git a/packages-private/template-explorer/package.json b/packages-private/template-explorer/package.json
index 04b87949..0ca59061 100644
--- a/packages-private/template-explorer/package.json
+++ b/packages-private/template-explorer/package.json
@@ -13,3 +13,3 @@
   "dependencies": {
-    "monaco-editor": "^0.55.1",
+    "monaco-editor": "^0
...
```
- **Reference:** `chore(deps): update dependency monaco-editor to ^0.56.0 (#15196)`
- **Base:** '.editorconfig: ^0.55.1\n+  monaco-editor: ^0.56.0'
- **Fine-tuned:** 'chore(deps): update dependencies (#14345)'
