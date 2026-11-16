# Qwen 4 Max 提示词写法：如何为视频提示 Qwen 4 Max

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Qwen 4 Max 不直接输出视频。它写代码，通常是一个 HTML 页面（用 Three.js、WebGL、Canvas 或 SVG），作者再把页面播放过程录下来。下面的写法来自作者随视频公开的提示词。每条都链接到它来源的帖子。本指南会随合集一起增长：只写已公开的提示词能支撑的内容，今后有更多作者公开提示词，再补充新的写法。

作者的设置各不相同（默认推理、high、`xhigh`，以及不同的 harness），设置会改变结果。第 7 条讲的就是把设置写下来。

## 1. 要求输出一个独立文件

说清格式，以及打开时要能做什么。这里不少出色的作品都是一个能从本地或 CDN 直接运行的文件：

- "single html file. use any libs via cdn"（[@analogalok][analogalok]），用于一个电动机动画。
- "build the crossy road game"，作者直接在浏览器里提示，并把生成的 HTML 文件下载下来（[@markksantos][markksantos]）。
- "Build a playable violin web app with Apple GarageBand inspired 3D graphical elements"（做一个可以演奏的小提琴网页应用，带有受 Apple GarageBand 启发的 3D 元素）（[@he1000se][he1000se]），在 OpenCode harness 中运行。

## 2. 点名渲染方式

同一个场景在 Three.js、原生 WebGL 和 SVG 里的效果不同，模型会按你点名的方式来做：

- 3D 场景用 Three.js：用代码构建的 3D 场景（太阳系测试用的是原生 WebGL，见 [@Frtnel][frtnel]）。
- 想自己控制渲染时，用原生 WebGL（[@Frtnel][frtnel]）。
- 小型、带动画的矢量页面用 SVG。鹈鹕测试要求"an animated SVG of a pelican riding a bicycle"，有作者只用这一句就拿到了一个完整的交互页面（[@xiangxiang103][xiangxiang]）。

## 3. 保持短需求，让它补全场景

短需求得到的是模型的选择，作者也是据此评价结果的。以下是完整的提示词：

- "Draw a beautiful nature scene in javascript"（[@badboy999654][badboy]）。
- "Generate a video of a pelican riding a bicycle"（[@atomic_chat_hq][atomic]）。这是鹈鹕测试的提示词，只是带了 "video" 一词；模型返回的是代码，而不是视频文件。

短提示词得到的是模型的选择，不是你的。某个细节重要，就把它写下来（见第 4 条）。

## 4. 写清楚物理规律和需要的细节

场景需要准确时，说明必须看得见什么。电动机提示词要求"showing everything clearly even the magnetic field, electrons etc."（[@analogalok][analogalok]）。作者认为模型在细节上做得不错，但另一款模型在写实度上更好，所以需求是杠杆，而不是保证。

## 5. 要求一次生成，并说明设置

想单独展示模型能力的作者，用的是一次调用、不做修正："Without using any external assets, all in code, no tool calls, no harness, single api call with high thinking effort"（[@ItsmeAjayKV][forest]）。森林场景和针对预览版的一次生成好评，都来自这种设置。

## 6. 报告 bug，不要替它修

构建失败时，描述你看到的现象，让模型修自己的代码。一个 Three.js 水母场景里，一次运行闪过黑框，另一次点击后屏幕变白。"1 bug report each and both fixed it, so the model can debug its own shaders when you point at the problem"（[@superalesha][jellyfish]）。

## 7. 把设置和结果一起记录

上面每个出色的结果都写明了设置。你也应该这样做，因为同一提示词换一个 harness 或换一个推理强度，就是另一场测试：

- "Qwen 4 Max (default reasoning, OpenCode harness)"，总计 172k token（[@he1000se][he1000se]）。
- "1 prompt, 1 model, xhigh effort"，Blender 通过 MCP 驱动（[@superalesha][ramen]）。
- "single api call with high thinking effort"（[@ItsmeAjayKV][forest]）。
- 一个 197K token 的 WebGL 太阳系，生成用了一个多小时（[@Frtnel][frtnel]）。

## 预算与录制

- **输出预算。** 作者的运行分别报告了 17.2 万和 19.7 万 token。[教程](tutorial.md)里的 curl 示例给到 `max_tokens: 128000`；页面更大时请再加大。
- **录制。** [`scripts/record.mjs`](../../scripts/record.mjs) 按你给的尺寸打开页面，录指定秒数，并转成 H.264 MP4（见[教程](tutorial.md#4-把页面录成视频)）。要求自动播放或定长循环，让画面不依赖鼠标。
- **成本。** 标价为每百万输入 token $1.666667、每百万输出 token $5。这里没有任何作者公布美元总额，请把 `usage` 字段按这些单价折算。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 low-poly / 电影感 / 霓虹]，[氛围、光照、配色]。
运动：[什么在动、怎么动]。加载后自动播放 [10] 秒的镜头巡游，然后循环。
交互：[拖拽 = …，滚轮 = …，点击 = …，按键 = …]。
规则：[必须遵守的数字：房间数、生命、波次、齿轮比、碰撞]。

技术：
- 使用 [CDN import map 以 ES module 引入的 Three.js / 原生 WebGL / SVG]，不要其他库。
- 不要外部图片、字体、音频：贴图用代码生成，声音用 Web Audio。
- 铺满视口，不出现滚动条。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 把它同时跑在 Qwen 4 Max 和其他模型上对比，或用[教程](tutorial.md)里的 API。

---

引文均为帖子中的短摘录并注明作者，完整提示词和视频请点链接。

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
