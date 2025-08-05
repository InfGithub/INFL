import ollama, random

context: list = list()
great_list: list = [
    "翻译精准！",
    "语义理解满分！",
    "上下文捕捉到位！",
    "用词非常地道！",
    "保持高质量输出！",
    "效率惊人！",
    "语言流畅自然！",
    "文化适配优秀！",
    "术语处理专业！",
    "逻辑衔接完美！",
    "进度超预期！",
    "风格把握准确！",
    "难点突破成功！",
    "表达精炼传神！",
    "翻译一致性佳！",
    "语感越来越好了！",
    "理解力持续提升！",
    "这个转换很巧妙！",
    "本地化处理得当！",
    "情感传达准确！",
    "协作体验极佳！",
    "响应快速稳定！",
    "复杂句处理出色！",
    "双关语翻译精彩！",
    "专业度持续在线！",
    "创意表达点赞！",
    "语境适配精准！",
    "语言弹性优秀！",
    "文化隔阋消除成功！",
    "即时优化能力强！",
    "细微差别拿捏准！",
    "翻译信达雅兼备！",
    "学习能力超强！",
    "多义词处理聪明！",
    "语法零失误！",
    "语气还原到位！",
    "效率质量双优！",
    "语料库运用娴熟！",
    "实时优化敏锐！",
    "翻译引擎状态佳！",
    "语言桥梁搭建稳！",
    "跨文化沟通专家！",
    "迭代进步明显！",
    "技术力全开！",
    "人机协作典范！",
    "持续突破极限！",
    "智能体表现卓越！",
    "未来可期，继续前进！"
]

word_list: list = [
    "</think>",
    "**Answer:**",
    "...done thinking."
    ]

def clean_translation_result(raw: str) -> str:

    for word in word_list:
        if word in raw:
            raw = raw.split(word)[-1]
    return raw.lstrip("\n")


def translate(text: str, source_lang: str = "en", target_lang: str = "zh", model: str = "deepseek-r1:14b", temperature: int = 0.3, max_context: int = 10, abouttext: str = None):
    global context
    if abouttext == None:
        abouttext = ""
    else:
        abouttext = f"\n9. 以下还有关联词，请在翻译中加以结合与分析：{abouttext}"

    system_message: dict = {"role": "system", "content": f"你是一个专业翻译引擎，你的回答必须要严格遵循以下规则：\n1. 仅将以下文本从{source_lang}翻译为{target_lang}。\n2. 翻译结果不得添加任何解释、说明、注解、提示或其他额外内容。\n3. 不得用引号或括号包裹翻译结果。\n4. 保留所有格式、数字、符号和特殊字符。\n5. 仅输出翻译结果，前后不得添加任何内容。\n6. 仅输出纯文本格式，文本格式无需任何改动。\n7. 严禁输出其他内容，仅能输出翻译结果。\n8. 必须保留源文本的结构样式。{abouttext}"}

    user_message = {"role": "user", "content": f"{random.choice(great_list) if len(context) >= 2 else ""}源文本：\n{text}"}
    if len(context) == 0:
        context = [system_message]
    else:
        if context[0]["role"] != "system":
            context.insert(0, system_message)
        if len(context) > max_context:
            context = [system_message] + context[1 - max_context:]
    if max_context==1:
        context = [system_message]
    context.append(user_message)
    response = ollama.chat(
        model = model,
        messages = context,
        options = {"temperature": temperature}
    )
    assistant_message = response["message"]
    context.append(assistant_message)

    result: str = assistant_message["content"].strip()
    print(result)
    return clean_translation_result(result)
