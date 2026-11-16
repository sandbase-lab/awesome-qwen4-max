# Qwen 4 Max vs Claude Opus 5.5, Claude Sonnet 5.5 and Gemini 4 Hydrogen

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, setups and token counts. Useful context, not verified by us.

The creators here tested the Qwen4-Max preview build, which the Lab collection lists as `alibaba/qwen4-max`. Every number below speaks for that build, not for a later general release.

## What we measured: Lab Evals boards and Pelican Test

**There is no Qwen 4 Max row on the Evals boards or the Pelican Test in the data this list was built from.** Nothing on this page can place Qwen 4 Max against the frontier from measurements. The rows below are rivals, copied from the snapshots recorded in the sibling lists (Evals snapshot 2026-10-19, Pelican Test read 2026-10-20). They are not refreshed for this page, so check the live boards before you rely on them.

Evals rows (Artificial Analysis snapshot, 2026-10-19):

| Model (row on the board) | [Intelligence Index][b-intel] | [Cost per task][b-cost] |
|---|---|---|
| **Qwen 4 Max** | **not on the board in this data** | — |
| Claude Opus 5.5 (Max) | 57.6 (#1) | $5.98 (#188) |
| Gemini 4 Argon (High) | 52.6 (#9) | $1.99 (#158) |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1 (#36) | $0.262 (#74) |

What this says, and what it doesn't: these are rivals, not the build the creators tested. They show where the frontier sits on the measured board, and nothing about Qwen 4 Max's score until it is measured.

Pelican Test rows (live leaderboard, read 2026-10-20, 22 models):

| Rank | Model | Results | Score | Avg cost |
|---|---|---|---|---|
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | $0.223 |
| 5 | deepseek/deepseek-v4.1-flash | 6 | 3.44 | $0.017 |
| — | **alibaba/qwen4-max** | **none in this data** | — | — |

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once static and once animated. It scores the rendered page 0 to 5 with an LLM judge on four questions: recognizable, actually riding, a bike that works, looks good. Cost is the real billed amount on SandBase. The Pelican Test is the quickest way to add a measured row for Qwen 4 Max: [run it yourself][pelican].

## What creators reported

Same-prompt comparisons and solo runs posted on X. Numbers are as the creator stated them: different harnesses (OpenCode, Qwen Code, a "DeepSeek Harness"), different reasoning settings, often one run. None of these posts includes a dollar figure, so the token counts are the only numbers here. Click through to watch both results.

| Creator | Task | Rival | What they reported |
|---|---|---|---|
| [@analogalok][analogalok] | Electric motor animation, one HTML file, "Qwen 4 Max vs Qwen 3.8 Max vs Gemini 4 Hydrogen" | Gemini 4 Hydrogen, Qwen 3.8 Max | "Gemini 4 Hydrogen did the best overall job on 3D realism and visual clarity" |
| [@markksantos][markksantos] | "build the crossy road game", prompted in the browser | Claude Opus 5.5 Medium | "I think Opus won this one. But it was definitely close!" |
| [@Frtnel][frtnel] | Interactive 3D solar system in raw WebGL, three models, same prompt | Claude Sonnet 5.5, Claude Opus 5.5 | Opus 5.5 judged Qwen's code quality close to Sonnet 5.5; 197K tokens in just over an hour |
| [@superalesha][ramen] | Ramen stall in Blender through Blender MCP, one prompt, xhigh effort | "DeepSeek Harness" (DSH) | "The DSH run honestly looks really good"; hopes the final release is more stable than the preview; 11.96M input tokens on the DSH run |
| [@superalesha][jellyfish] | Deep-ocean jellyfish scene in Three.js, same prompt in two harnesses, both xhigh | "DeepSeek Harness" (DSH) | Qwen Code flashed black boxes; each run needed one bug report to fix |
| [@atomic_chat_hq][atomic] | Pelican benchmark: "Generate a video of a pelican riding a bicycle" | Claude Opus 5.5 | No verdict in the post text |

Solo runs and quality notes, without a rival:

- [@ItsmeAjayKV][forest] ran a forest scene as "a single api call with high thinking effort" and said "Qwen4-max-preview is great on one-shots".
- [@he1000se][he1000se] built a playable violin web app with 3D elements in the OpenCode harness at default reasoning, 172k tokens.
- [@xiangxiang103][xiangxiang] ran the pelican prompt and got a full interactive page with 18 live sliders. The creator noted the pelican's body is oversized, and said the official launch did not publish parameters or benchmark scores.
- [@Aurora0x3f][aurora] ran the pelican test in SVG and said it felt "a bit faster" than the preview.
- [@badboy999654][badboy] shared a one-shot nature scene in JavaScript.

The pattern across these posts: creators are most positive about one-shot and single-file builds and split on the top models. Where a creator preferred a rival, it was on realism (Gemini 4 Hydrogen in the electric motor test) or the final result of a longer run (Opus 5.5 in the Crossy Road test). Nobody here reports a measured score.

## Rerun before you trust a comparison

Results move with the setup. A single run per model, a different harness, or a different reasoning effort can flip the result. Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals]: Artificial Analysis data. Search for "Qwen" to see whether a row has been added since this page was written.
- [Lab Pelican Test][pelican]: same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections]: the same list for other models.

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-19 for the rival rows) and [Pelican Test][pelican] (read 2026-10-20 for the rival rows). Creator data: their posts, linked; not independently verified.

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
