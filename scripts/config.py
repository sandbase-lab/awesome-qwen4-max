"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'qwen4-max'
REPO = 'sandbase-lab/awesome-qwen4-max'

CFG = dict(
    slug=SLUG,
    name='Qwen 4 Max',
    short='Qwen 4 Max',  # how the prose refers to the model after the first mention
    vendor='Qwen (Alibaba)',
    model_id='alibaba/qwen4-max',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-qwen4-max',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/alibaba/qwen4-max',
    arena=f'{SITE}/arena/text?models=alibaba%2Fqwen4-max',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-qwen4-max-sync/1.0 (+https://github.com/{REPO})',
    html_out='qwen4-max.html',
    # Output limit for the curl example. Creators' Qwen 4 Max runs reported 172K and 197K tokens
    # (@he1000se, @Frtnel), so 128,000 is the budget the example asks for; raise it for long pages.
    max_tokens=128000,
    # Not in the collection data (facts.json: max_tokens null). Fill from
    # `sandbase inspect alibaba/qwen4-max --json` (inputSchema.max_tokens.maximum) before publishing.
    max_tokens_limit=None,
    context_length=1000000,  # facts.json: context_length, from `sandbase inspect`
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Qwen 4 Max',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'grok', 'qwen', 'qwen4', 'glm',
                 'hydrogen'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Qwen (Alibaba).',
                    'zh-CN': '与 Qwen（阿里巴巴）无隶属或背书关系。'},
    # No SandBase blog post on this model is in the collection data. build_readme.py skips the
    # reading section while this is empty; do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: facts.json (inspect values, the collection's own posts, linked),
# and the creator posts linked in docs/. There is no Qwen 4 Max row on the Lab Evals boards or
# the Pelican Test yet, and no dollar figures appear in the creator posts.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Qwen 4 Max examples**: videos, prompts and demos made with Qwen4-Max, Alibaba\'s Qwen 4 Max model, announced on November 11, 2026 and tested by creators in preview. Three.js and WebGL 3D scenes, SVG and canvas animation, motion graphics, product UI and playable browser games, most of them written as one self-contained HTML page from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Qwen 4 Max: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[Qwen 4 Max vs. Claude Opus 5.5, Claude Sonnet 5.5 and Gemini 4 Hydrogen](docs/model-comparison.md)'),
            ('Try it now', '[Run Qwen 4 Max in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. The call above asks for 128,000 `max_tokens` because creators\' runs reported 172K and 197K tokens; raise it for long pages. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Qwen 4 Max?', 'Qwen4-Max is Alibaba\'s Qwen 4 Max model. The Lab collection was announced on November 11, 2026, and the creators here tested the preview build; @xiangxiang103 reports it launched in preview on Qoder and says no parameter count or benchmark scores were published. SandBase lists a context window of 1,000,000 tokens. On SandBase it is `{model_id}`. Source: `sandbase inspect alibaba/qwen4-max`.'),
            ('How are these Qwen 4 Max videos made?', 'The model doesn\'t render video. It writes code, usually one HTML page (Three.js, WebGL, canvas or SVG), and the creator records the page playing. Some creators ran it through a coding harness such as OpenCode or Qwen Code, and one drove Blender through an MCP connection. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Qwen 4 Max prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js, WebGL, canvas or SVG), state the constraints, ask for a one-shot build with no fixes, and say which harness and reasoning setting you used. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Qwen 4 Max API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint, and one key works for every model. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Qwen 4 Max better than Claude Opus 5.5, Claude Sonnet 5.5 or Gemini 4 Hydrogen?', 'Creators disagree. In an electric-motor test @analogalok found Gemini 4 Hydrogen did the best overall job on 3D realism and clarity. @markksantos says Opus won a Crossy Road build, "but it was definitely close". @Frtnel reports Opus 5.5 judged its WebGL solar system to be close to Sonnet 5.5. The Lab [Evals boards]({evals}) and [Pelican Test]({pelican}) had no Qwen 4 Max row when this list was built. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'The list price on SandBase is $1.666667 per million input tokens and $5 per million output tokens, and cached input reads bill at 5% of the input rate. Creators in this collection posted token counts, not dollar totals, so multiply the `usage` field by those rates. Source: `sandbase inspect alibaba/qwen4-max` and the model page.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Qwen 4 Max creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Qwen 4 Max prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Qwen 4 Max videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Qwen 4 Max 案例**合集：用 Qwen4-Max（阿里巴巴的 Qwen 4 Max 模型，11 月 11 日公布，创作者在预览版上测试）做出的视频、提示词和演示。包括 Three.js 与 WebGL 3D 场景、SVG 与 Canvas 动画、动效、产品界面和可在浏览器里玩的游戏，大多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome Qwen 4 Max：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[Qwen 4 Max 对比 Claude Opus 5.5、Claude Sonnet 5.5 和 Gemini 4 Hydrogen](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Qwen 4 Max]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。上面的示例给到 128,000 `max_tokens`，因为作者的运行分别报告了 17.2 万和 19.7 万 token；长页面请再加大。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Qwen 4 Max 是什么？', 'Qwen4-Max 是阿里巴巴的 Qwen 4 Max 模型。Lab 合集于 2026 年 11 月 11 日公布，这里的创作者测试的是预览版；@xiangxiang103 称它在 Qoder 上以预览形式首发，并表示官方没有公布参数量和跑分。SandBase 标注的上下文窗口为 100 万 token。在 SandBase 上它是 `{model_id}`。来源：`sandbase inspect alibaba/qwen4-max`。'),
            ('这些 Qwen 4 Max 视频是怎么做出来的？', '模型并不直接渲染视频。它写出代码，通常是一个 HTML 页面（Three.js、WebGL、Canvas 或 SVG），作者再把页面播放过程录下来。有作者通过 OpenCode、Qwen Code 等编码 harness 运行，也有人通过 MCP 连接让它驱动 Blender。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Qwen 4 Max 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪个渲染方式（Three.js、WebGL、Canvas 或 SVG）；写明约束，要求一次生成、不做修正；并说明用的是哪个 harness 和推理强度。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Qwen 4 Max API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Qwen 4 Max 比 Claude Opus 5.5、Claude Sonnet 5.5 或 Gemini 4 Hydrogen 更强吗？', '作者们的结论不一致。@analogalok 在一个电动机测试里发现 Gemini 4 Hydrogen 在 3D 写实度和清晰度上整体最好；@markksantos 说 Opus 赢了一个 Crossy Road 版本，"但真的很接近"；@Frtnel 报告 Opus 5.5 认为它的 WebGL 太阳系代码质量与 Sonnet 5.5 接近。创建本列表时，Lab [Evals 榜单]({evals}) 和 [Pelican Test]({pelican}) 都还没有 Qwen 4 Max 的数据行。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', 'SandBase 标价为每百万输入 token $1.666667、每百万输出 token $5，缓存命中的输入按输入价的 5% 计费。本合集的作者公布的是 token 数量而非美元总额，所以请把 `usage` 字段按这些单价折算。来源：`sandbase inspect alibaba/qwen4-max` 和模型页。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Qwen 4 Max 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Qwen 4 Max 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Qwen 4 Max 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
