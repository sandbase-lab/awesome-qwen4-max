# Qwen 4 Max 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。Qwen 4 Max 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 Qwen 4 Max。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 Qwen 4 Max 旁边再加一两个模型（例如 `anthropic/claude-opus-5.5` 或 `deepseek/deepseek-v4.1-flash`），跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。合集里 46 条视频中有 20 条属于"测试对比"分类，作者们也是这样做的对比；[对比页](model-comparison.md)列出了他们报告的结果。在你自己的任务上跑同一个提示词，是验证结论最快的方式。

## 3. 或者直接调用 API

Qwen 4 Max 在 SandBase 上的模型 ID 是 `alibaba/qwen4-max`，兼容 OpenAI，上下文窗口 100 万 token。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "alibaba/qwen4-max",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > qwen4-max.html
jq '.usage' response.json
```

- `max_tokens: 128000`：作者的运行分别报告了 17.2 万和 19.7 万 token，所以给长页面留足空间。提高上限前，先用 `sandbase inspect alibaba/qwen4-max` 查看上限。
- `--max-time 900`：一个长页面可能需要十几分钟以上。有一次太阳系运行用了一个多小时（[@Frtnel][frtnel]）。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token。价格见[模型页][model]：每百万输入 token $1.666667，每百万输出 token $5。

用浏览器打开 `qwen4-max.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联）。

### 用 SandBase CLI

同一个调用也可以走 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli)，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect alibaba/qwen4-max   # 输入字段和价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_alibaba_qwen4_max -f input.json --timeout 900 -o result.json
```

`-o result.json` 保存响应；页面在 assistant 消息里，和 API 一样。工具名遵循 `sandbase_<模型 ID>` 的规则，先用 `inspect` 确认。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs qwen4-max.html qwen4-max.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动镜头巡游或定长循环（见[提示词写法 §4](prompt-guide.md#4-写清楚物理规律和需要的细节)），让整个画面不依赖鼠标。

录制本身只有画面。需要声音的话，在剪辑里加音频。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ Qwen 4 Max。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-qwen4-max/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/qwen4-max?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[arena]: https://www.sandbase.ai/arena/text?models=alibaba%2Fqwen4-max&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[model]: https://www.sandbase.ai/model/alibaba/qwen4-max?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[frtnel]: https://x.com/Frtnel/status/2122213962011881801
