# Qwen 4 Max 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 12 条 Qwen 4 Max 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 Qwen 4 Max 一键 **复刻**。第一次写 Qwen 4 Max 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (3)
- [动效](#motion-graphics) (2)
- [产品界面](#ui-demo) (1)
- [文字动效](#kinetic-type) (1)
- [测试对比](#comparison) (5)

<a id="3d-scene"></a>

## 3D 场景

### 深秋时节的枫树与白桦树林

[@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2120448740012265621) · 1:36 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2120448740012265621/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2120448740012265621?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen4-max-preview is great on one-shots🔥

Another one-shot result and Qwen4-max-preview again impressed me.

I asked it to make a maple and birch forest at peak autumn, with trees and some nice animation, goal is to build a forest that has life to it. 

Without using any external assets, all in code, no tool calls, no harness, single api call with high thinking effort. 

I have done the same with other models, deepseek-v4.1-flash produced the best result, until now, we have a new winner.

Qwen absolutely went crazy and added so many extra features, extra sound, all the controls, everything towards making this feel more whole. Nothing wasted.

And this entire thing only needed 83,173 tokens.

This is lower than what DeepSeek-v4.1-flash-1017 required.
```

### Blender程序化拉面摊微缩场景

[@superalesha](https://x.com/superalesha/status/2120666965060559213) · 0:37 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2120666965060559213/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2120666965060559213?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen4-Max just built a full ramen stall in Blender. No assets, only code through Blender MCP.

1 prompt, 1 model, xhigh effort. Left: DeepSeek Harness. Right: Qwen Code.

The DSH run honestly looks really good. All the confused and unhappy voices about Qwen4 right now, mine included, I really hope it is just the preview, and GA comes out better and more stable.

Tokens, DSH: 11.96M input, 11.59M cached, 130K output
Tokens, Qwen Code: 3.02M input, 2.85M cached, 62K output

Prompt:
Using only the Blender MCP tools (the blender tools you have), build a cozy night diorama in Blender: a tiny ramen stall on a rainy street corner in Tokyo, on a square base like a miniature. Model everything procedurally with Python in Blender, do not import or generate assets. Include the wooden stall with a cloth noren curtain, paper lanterns, steaming bowls, stools, a vending machine, wet asphalt with puddles that reflect the neon signs, and falling rain. Use proper materials and warm and neon lighting, render with Cycles on the GPU. Deliver into your folder: a 1920x1080 final still, and a 6-second 24 fps 1280x720 camera move around the diorama encoded as an MP4. Check your renders by looking at them and fix what looks wrong.
```

### Three.js 深海发光水母群

[@superalesha](https://x.com/superalesha/status/2120718224031715706) · 0:37 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2120718224031715706/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2120718224031715706?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen4-Max made a deep ocean full of glowing jellyfish in Three.js. Same prompt in 2 harnesses.

Top: DeepSeek Harness. Bottom: Qwen Code. Both on xhigh.

The Qwen Code version flashed black boxes for 1 frame at a time, the DSH one blew the screen white on click. 1 bug report each and both fixed it, so the model can debug its own shaders when you point at the problem.

Tokens, DSH: 11.22M input, 10.80M cached, 110K output
Tokens, Qwen Code: 10.84M input, 10.18M cached, 121K output

Prompt:
Create a deep-ocean scene in Three.js, in a single HTML file: a swarm of bioluminescent jellyfish drifting through dark blue water. Each jellyfish has a soft, pulsing bell made with a vertex shader and long tentacles simulated with verlet physics that trail and sway as it swims. Add glowing light patterns that ripple across the bells, volumetric light shafts from the surface far above, drifting marine snow particles, depth fog and bloom. Moving the mouse creates a gentle current that pushes the jellyfish and bends their tentacles; clicking makes the nearest ones flash and dart away. Keep it smooth at 60 fps. When you are done, open the page in the browser, look at screenshots and fix what looks wrong.
```

<a id="motion-graphics"></a>

## 动效

### JavaScript绘制的美丽自然风景

[@badboy999654](https://x.com/badboy999654/status/2121475034296520920) · 2:48 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2121475034296520920/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2121475034296520920?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
“Draw a beautiful nature scene in javascript"   - Qwen 4 max prewiev on the web. 
Anthropic 6 centuries ahead fanboys are in for a hard one.
```

### SVG鹈鹕骑自行车2D动画

[@Aurora0x3f](https://x.com/Aurora0x3f/status/2122169039061750020) · 0:38 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122169039061750020/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122169039061750020?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max，先简单来个最传统的鹈鹕测试

提示词依旧：创建一个HTML，内容是SVG绘制一个鹈鹕骑自行车的2D动画

跟 preview 相比我体感是快了一些
```

<a id="ui-demo"></a>

## 产品界面

### 包含3D元素的可演奏小提琴网页应用

[@he1000se](https://x.com/he1000se/status/2122164935761260584) · 0:28 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122164935761260584/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122164935761260584?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max (default reasoning, OpenCode harness) 

Prompt: A playable violin web app with Apple Garageband inspired 3D graphical elements 

172k tokens
```

<a id="kinetic-type"></a>

## 文字动效

### 一只骑自行车的鹈鹕的 动画SVG

[@xiangxiang103](https://x.com/xiangxiang103/status/2120414419230605560) · 2:01 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2120414419230605560/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2120414419230605560?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen4-Max-Preview 今天在 Qoder 首发预览，属实太能加戏了！

官方说知识更深、编程和智能体能力更强，没公布参数和跑分。我试了下老规矩，只喂一句鹈鹕骑车测试题：Generate an animated SVG of a pelican riding a bicycle

结果不止画张图，直接交了个完整交互网页：
大黄喙鹈鹕戴红头盔系蓝围巾、车筐装鱼，背景有夕阳、海边栈桥、棕榈树、海鸥和木栈道，车轮链条踏板都在动，双脚始终踩在踏板上。右侧带 18 个实时滑块调车速齿比和翅膀摆动、4 套配色，点车铃会响、点鹈鹕会叫，有快捷键，还能导出动画 SVG 和 2 倍 PNG。

缺点是身体偏大，挡住车座和后半个车架，看着像浮在车上😂

一句提示词卷成这样，你们打几分？
```

<a id="comparison"></a>

## 测试对比

### AI模型生成的天天过马路游戏对比

[@markksantos](https://x.com/markksantos/status/2120446429718086142) · 0:40 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2120446429718086142/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2120446429718086142?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max Preview vs. Claude Opus 5.5 Medium

I prompted from the browser and then downloaded the HTML file it generated.

Prompt: "build the crossy road game"

I think Opus won this one. But it was definitely close!

What did you think?
```

### 原生WebGL交互式3D太阳系代码对比

[@Frtnel](https://x.com/Frtnel/status/2122213962011881801) · 1:08 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122213962011881801/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122213962011881801?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max Preview just made a coding comparison with Claude Sonnet 5.5 and Opus 5.5 a lot more interesting.

This dev gave all three models the same prompt to build an interactive 3D solar system using raw WebGL.

Opus 5.5 judged Qwen’s code quality to be close to Sonnet 5.5. Qwen generated 197K tokens in just over an hour.

How much longer can frontier models maintain their coding advantage?
```

### 电动马达动画与物理模拟对比

[@analogalok](https://x.com/analogalok/status/2122221106304352257) · 0:13 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122221106304352257/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122221106304352257?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max Vs Qwen 3.8 Max Vs Gemini 4 Hydrogen

Prompt:
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn

Gemini 4 Hydrogen did the best overall job on 3D realism and visual clarity, modeling a proper curved horseshoe magnet, detailed commutator, and phase by phase physics explanations without visual clutter. 

Qwen 4 Max offered the richest lab dashboard, adding a physical DC battery, live waveform graph, and friction controls though its dense glowing overlays crowded the center. Qwen 3.8 Max had the simplest 3D scene but stood out for its helpful synchronized 2D schematic view.
```

### Qwen 4 Max与Claude Opus 5.5骑车鹈鹕对比

[@atomic_chat_hq](https://x.com/atomic_chat_hq/status/2122275275132072029) · 0:07 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122275275132072029/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122275275132072029?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max vs Claude Opus 5.5 on the PELICAN BENCHMARK 🐦🚲

Prompt: Generate a video of a pelican riding a bicycle

Run AI models locally → https://t.co/RbcCOIgVkj
```

### Qwen 4 Max与Claude Opus 5.5骑车鹈鹕对比

[@atomic_chat_hq](https://x.com/atomic_chat_hq/status/2122278047403348332) · 0:07 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122278047403348332/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/qwen4-max/2122278047403348332?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max&utm_content=prompt-index)

```text
Qwen 4 Max vs Claude Opus 5.5 on the PELICAN BENCHMARK 🐦🚲

Prompt: Generate a video of a pelican riding a bicycle

Run AI models locally → https://t.co/RbcCOIgVkj
```
