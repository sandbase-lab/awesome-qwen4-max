# Qwen 4 Max tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Qwen 4 Max writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Qwen 4 Max selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to Qwen 4 Max (for example `anthropic/claude-opus-5.5` or `deepseek/deepseek-v4.1-flash`) and run once. Every model gets the same words, and each result shows its cost and time. Creators here ran this same kind of head-to-head: 20 of the 46 videos are in the Tests & comparisons category, and the [comparison page](model-comparison.md) lists what they reported. Running the same prompt yourself is the quickest way to check a claim on your own task.

## 3. Or call the API

Qwen 4 Max is `alibaba/qwen4-max` on SandBase, OpenAI-compatible, with a 1,000,000-token context window.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

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

- `max_tokens: 128000`: the creators' runs reported 172K and 197K tokens, so give a long page room. Check the cap with `sandbase inspect alibaba/qwen4-max` before you raise it.
- `--max-time 900`: one long page can take well over ten minutes. One creator's solar-system run took just over an hour ([@Frtnel][frtnel]).
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for. Prices are on the [model page][model]: $1.666667 per million input tokens and $5 per million output tokens.

Open `qwen4-max.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline).

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect alibaba/qwen4-max   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_alibaba_qwen4_max -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API. The tool name follows the `sandbase_<model id>` pattern; confirm it with `inspect` first.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs qwen4-max.html qwen4-max.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §4](prompt-guide.md#4-spell-out-the-physics-and-the-details-you-need)), so nothing depends on a mouse.

The recording is picture only. Add audio in the edit if you want sound.

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Qwen 4 Max. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-qwen4-max/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/qwen4-max?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[arena]: https://www.sandbase.ai/arena/text?models=alibaba%2Fqwen4-max&utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[model]: https://www.sandbase.ai/model/alibaba/qwen4-max?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-qwen4-max
[frtnel]: https://x.com/Frtnel/status/2122213962011881801
