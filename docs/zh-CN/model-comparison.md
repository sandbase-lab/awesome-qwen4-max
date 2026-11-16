# Qwen 4 Max 对比 Claude Opus 5.5、Claude Sonnet 5.5 和 Gemini 4 Hydrogen

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的同提示词对比和单项运行，附他们自己的 harness、设置和 token 数。有参考价值，但我们没有验证。

这里的创作者测试的是 Qwen4-Max 预览版，Lab 合集把它标为 `alibaba/qwen4-max`。下面所有数字都只说明那个预览版，不代表之后的正式版。

## 我们测到的：Lab Evals 榜单与 Pelican Test

**在本列表所依据的数据里，Lab Evals 榜单和 Pelican Test 都没有 Qwen 4 Max 这一行。** 因此，单凭实测无法把 Qwen 4 Max 和前沿模型排在一起。下面的行是竞品，取自同类合集里记录的快照（Evals 快照 2026-10-19，Pelican Test 2026-10-20 读取）。这些数字没有为本页刷新，依赖之前请先查看实时榜单。

Evals 行（Artificial Analysis 快照，2026-10-19）：

| 模型（榜单上的行） | [智能指数][b-intel] | [单任务成本][b-cost] |
|---|---|---|
| **Qwen 4 Max** | **本数据中不在榜上** | — |
| Claude Opus 5.5 (Max) | 57.6（第 1） | $5.98（第 188） |
| Gemini 4 Argon (High) | 52.6（第 9） | $1.99（第 158） |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1（第 36） | $0.262（第 74） |

这说明什么、不说明什么：这些是竞品，不是作者们测试的那个构建。它们只说明实测榜单上前沿的位置，在 Qwen 4 Max 被测之前，不能说明它的分数。

Pelican Test 行（实时榜单，2026-10-20 读取，22 个模型）：

| 排名 | 模型 | 结果数 | 得分 | 平均成本 |
|---|---|---|---|---|
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | $0.223 |
| 5 | deepseek/deepseek-v4.1-flash | 6 | 3.44 | $0.017 |
| — | **alibaba/qwen4-max** | **本数据中没有** | — | — |

[Pelican Test][pelican] 让每个模型生成一只骑自行车的鹈鹕的 SVG，一次静态、一次动画。渲染后的页面由 LLM 裁判按四个问题打 0–5 分：能认出是鹈鹕、真的在骑、自行车结构成立、好看。成本是 SandBase 上的实际计费金额。要为 Qwen 4 Max 添加一行实测数据，Pelican Test 是最快的途径：[自己跑一次][pelican]。

## 创作者报告的

发在 X 上的同提示词对比和单项运行。数字按创作者自述：harness 不同（OpenCode、Qwen Code、"DeepSeek Harness"），推理设置不同，往往只跑一次。这些帖子都没有给出美元金额，所以这里的数字只有 token 数。点进链接可以两边一起看。

| 创作者 | 任务 | 对手 | 创作者报告 |
|---|---|---|---|
| [@analogalok][analogalok] | 电动机动画，单 HTML 文件，"Qwen 4 Max vs Qwen 3.8 Max vs Gemini 4 Hydrogen" | Gemini 4 Hydrogen、Qwen 3.8 Max | "Gemini 4 Hydrogen did the best overall job on 3D realism and visual clarity"（3D 写实度和视觉清晰度上整体最好） |
| [@markksantos][markksantos] | "build the crossy road game"，在浏览器里提示 | Claude Opus 5.5 Medium | "I think Opus won this one. But it was definitely close!"（我觉得 Opus 赢了，但真的很接近！） |
| [@Frtnel][frtnel] | 原生 WebGL 交互式 3D 太阳系，三个模型，同一提示词 | Claude Sonnet 5.5、Claude Opus 5.5 | Opus 5.5 认为 Qwen 的代码质量接近 Sonnet 5.5；生成 197K token，用时一个多小时 |
| [@superalesha][ramen] | 通过 Blender MCP 做拉面摊，一个提示词，xhigh 设置 | "DeepSeek Harness"（DSH） | "The DSH run honestly looks really good"（DSH 的运行效果确实很好）；希望正式版比预览版更稳定；DSH 那次运行输入 11.96M token |
| [@superalesha][jellyfish] | Three.js 深海水母场景，两个 harness 跑同一提示词，都是 xhigh | "DeepSeek Harness"（DSH） | Qwen Code 版闪过黑框；两边各用一条 bug 报告修好 |
| [@atomic_chat_hq][atomic] | 鹈鹕测试："Generate a video of a pelican riding a bicycle" | Claude Opus 5.5 | 帖子正文里没有结论 |

没有对手的单项运行与质量评价：

- [@ItsmeAjayKV][forest] 用"单次 API 调用、高思考强度"生成了一个森林场景，并称"Qwen4-max-preview is great on one-shots"（预览版的一次生成很强）。
- [@he1000se][he1000se] 在 OpenCode harness 中以默认推理做出一个可演奏的小提琴网页应用，带 3D 元素，共 172k token。
- [@xiangxiang103][xiangxiang] 跑了鹈鹕提示词，得到一个带 18 个实时滑块的完整交互页面。作者指出鹈鹕的身体偏大，并表示官方发布时没有公布参数量和跑分。
- [@Aurora0x3f][aurora] 用 SVG 跑了鹈鹕测试，说比预览版"快了一些"。
- [@badboy999654][badboy] 分享了一个一次生成的 JavaScript 自然场景。

这些帖子的共同规律：作者对一次生成和单文件构建最为正面，对顶级模型的看法则有分歧。倾向竞品的地方，一是写实度（电动机测试里的 Gemini 4 Hydrogen），二是较长运行的最终结果（Crossy Road 测试里的 Opus 5.5）。这里没有人报告实测分数。

## 对比前先重跑一次

结果会随设置变化。每个模型只跑一次、换一个 harness 或换一个推理强度，都可能让结论翻转。自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]：Artificial Analysis 数据。搜索 "Qwen"，看看之后是否已有新行。
- [Lab Pelican Test][pelican]：同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集][collections]：其他模型的同类列表。

---

Lab 数据：[Evals 榜单][evals]（竞品行为 Artificial Analysis 2026-10-19 快照）与 [Pelican Test][pelican]（竞品行为 2026-10-20 读取）。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

[evals]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[b-intel]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[b-cost]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[pelican]: https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[arena]: https://www.sandbase.ai/arena/text?models=alibaba%2Fqwen4-max&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[analogalok]: https://x.com/analogalok/status/2122221106304352257
[markksantos]: https://x.com/markksantos/status/2120446429718086142
[frtnel]: https://x.com/Frtnel/status/2122213962011881801
[ramen]: https://x.com/superalesha/status/2120666965060559213
[jellyfish]: https://x.com/superalesha/status/2120718224031715706
[atomic]: https://x.com/atomic_chat_hq/status/2122278047403348332
[forest]: https://x.com/ItsmeAjayKV/status/2120448740012265621
[he1000se]: https://x.com/he1000se/status/2122164935761260584
[xiangxiang]: https://x.com/xiangxiang103/status/2120414419230605560
[aurora]: https://x.com/Aurora0x3f/status/2122169039061750020
[badboy]: https://x.com/badboy999654/status/2121475034296520920
