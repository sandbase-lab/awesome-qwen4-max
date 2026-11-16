# Qwen 4 Max prompt guide: how to prompt Qwen 4 Max for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Qwen 4 Max doesn't output video. It writes code, usually one HTML page with Three.js, WebGL, canvas or SVG, and the creator records that page playing. The patterns below come from prompts creators posted with their videos. Each example links to the post it came from. This guide grows with the collection: it only covers what the shared prompts support, and new patterns will be added as more creators share theirs.

Creators' settings varied (default reasoning, high, `xhigh`, different harnesses), and the setting changes the result. Pattern 7 is about recording it.

## 1. Ask for one self-contained file

Name the format and what it must do when opened. Several strong pieces here were a single file that runs from disk or a CDN:

- "single html file. use any libs via cdn" ([@analogalok][analogalok]), on an electric motor animation.
- "build the crossy road game", which the creator downloaded as an HTML file straight from the browser ([@markksantos][markksantos]).
- "Build a playable violin web app with Apple GarageBand inspired 3D graphical elements" ([@he1000se][he1000se]), run in the OpenCode harness.

## 2. Name the renderer

The same scene looks different in Three.js, raw WebGL and SVG, and the model builds whichever you name:

- Three.js for a 3D scene: "a living koi pond" style scenes in code (the solar-system test was raw WebGL, see [@Frtnel][frtnel]).
- Raw WebGL when you want to control the rendering yourself ([@Frtnel][frtnel]).
- SVG for a small, animated vector page. The pelican test asks for "an animated SVG of a pelican riding a bicycle", and one creator got a full interactive page from that single line ([@xiangxiang103][xiangxiang]).

## 3. Keep a short brief and let it fill in the scene

Short briefs got the model's choices, and creators judged the results on that basis. These are the whole prompts:

- "Draw a beautiful nature scene in javascript" ([@badboy999654][badboy]).
- "Generate a video of a pelican riding a bicycle" ([@atomic_chat_hq][atomic]). This is the Pelican Test prompt with the word "video" in it; the model answers with code, not a video file.

Short prompts give you the model's choices, not yours. When a detail matters, write it down (pattern 4).

## 4. Spell out the physics and the details you need

Where the scene has to be accurate, name what must be visible. The electric-motor prompt asked for "showing everything clearly even the magnetic field, electrons etc." ([@analogalok][analogalok]). The creator found the model did well on detail, but a competitor did better on realism, so the brief is the lever, not a guarantee.

## 5. Ask for a one-shot build and say so

Creators who wanted to show the model alone used one call and no fixes: "Without using any external assets, all in code, no tool calls, no harness, single api call with high thinking effort" ([@ItsmeAjayKV][forest]). The forest scene and the one-shot comments on the preview build came from that setup.

## 6. Report the bug, not the fix

When a build fails, describe what you see and let the model fix its own code. In a Three.js jellyfish scene, one of the runs flashed black boxes and the other turned the screen white on click. "1 bug report each and both fixed it, so the model can debug its own shaders when you point at the problem" ([@superalesha][jellyfish]).

## 7. Record the setup next to the result

Every strong result above names its setup. Do the same, because the same prompt in a different harness or at a different effort is a different test:

- "Qwen 4 Max (default reasoning, OpenCode harness)", with a total of 172k tokens ([@he1000se][he1000se]).
- "1 prompt, 1 model, xhigh effort", with a Blender run driven through MCP ([@superalesha][ramen]).
- "single api call with high thinking effort" ([@ItsmeAjayKV][forest]).
- A 197K-token WebGL solar system that took just over an hour to generate ([@Frtnel][frtnel]).

## Budget and recording

- **Output budget.** The creators' runs reported 172K and 197K tokens. The curl example in the [tutorial](tutorial.md) asks for `max_tokens: 128000`; raise it for larger pages.
- **Recording.** [`scripts/record.mjs`](../scripts/record.mjs) opens the page at the size you give, records for N seconds and converts to H.264 (see the [tutorial](tutorial.md#4-turn-the-page-into-a-video)). Ask for an autoplay or a fixed-length loop, so nothing depends on a mouse.
- **Cost.** The list price is $1.666667 per million input tokens and $5 per million output tokens. No creator here posted a dollar total, so multiply the `usage` field by those rates.

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. low-poly / cinematic / neon], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second camera tour on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …].
Rules: [the numbers it must respect: rooms, lives, waves, gear ratios, collisions].

Technical:
- Use [Three.js as an ES module from a CDN import map / raw WebGL / SVG] and no other libraries.
- No external images, fonts or audio: generate textures in code, sound with Web Audio.
- Fill the viewport, no scrolling.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it in the [Lab text arena][arena] to run it on Qwen 4 Max and other models side by side, or with the API in the [tutorial](tutorial.md).

---

Quotes are short excerpts from the posts, credited to their authors. Follow the links for the full posts and videos.

[analogalok]: https://x.com/analogalok/status/2122221106304352257
[markksantos]: https://x.com/markksantos/status/2120446429718086142
[he1000se]: https://x.com/he1000se/status/2122164935761260584
[frtnel]: https://x.com/Frtnel/status/2122213962011881801
[xiangxiang]: https://x.com/xiangxiang103/status/2120414419230605560
[badboy]: https://x.com/badboy999654/status/2121475034296520920
[atomic]: https://x.com/atomic_chat_hq/status/2122278047403348332
[forest]: https://x.com/ItsmeAjayKV/status/2120448740012265621
[jellyfish]: https://x.com/superalesha/status/2120718224031715706
[ramen]: https://x.com/superalesha/status/2120666965060559213
[arena]: https://www.sandbase.ai/arena/text?models=alibaba%2Fqwen4-max&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
