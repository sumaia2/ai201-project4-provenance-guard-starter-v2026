"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Ten pieces I wrote myself, each at least 100 words.
        "texts": [
            "Soft, spiced, and topped with a buttery pecan crunch 🧡 These Pumpkin Muffins are the perfect fall bake—sweet, nutty, and impossible to resist! 🍁 Would you grab one (or two)? 😋👇",
            "Cozy vibes in a bowl ✨ This Creamy Roasted Pumpkin Soup with cinnamon & nutmeg is the ultimate fall comfort food 🍁🥣",
            "Cold nights call for something warm + hearty 💛 This Root Vegetable Lentil Stew is packed with protein, cozy spices, and fall veggies that make every spoonful feel like a hug in a bowl 🥣🍂",
            "Skip the coffee shop and make your own Pumpkin Spice Latte at home 🎃☕ It's creamy, cozy, and packed with those sweet fall spices you love 🍂✨",
            "✨ Cozy in a bowl ✨ This creamy Butternut Squash Soup with a hint of cinnamon & nutmeg is the ultimate fall comfort food 🍂🥣 Perfect for chilly evenings and easy enough for a weeknight dinner! Would you try this at home? 👇",
            "Chicken fettuccine Alfredo ♥️ #reelsinstagram #reels #cooking #spicyfood #recipe #chickenalfredo #fettuccinealfredo",
            "Thanksgiving side dishes 😋 Candied Yams 🍠 😋 #reelsinstagram #reels #cooking #thanksgiving #candiedyams #thanksgivingrecipes",
            "Indomie noodles with shin broth and soup base. Plus, eggs and shrimp 🍤 😋 #reelsinstagram #reels #cooking #spicyfood #recipe #indomiegoreng #shinramen #noodlerecipe",
            "Motherhood is a struggle #reels #cooking",
            "Crispy Nigerian Meat Pie #ramadan",
        ],
    },
    {
        "name": "AI-generated text",
        "criterion": 2,
        # Five pieces written by an AI tool (Claude), about 100 words each.
        # Criterion 2 compares their average score with the first five of my own pieces.
        "texts": [
            "Time management is one of the most important skills a person can develop. It allows individuals to balance their responsibilities and reduce stress. By setting clear priorities, people can focus on the tasks that matter most. Creating a daily schedule also helps to maintain consistency and avoid procrastination. In addition, breaking large projects into smaller steps makes them easier to complete. It is also important to take regular breaks in order to stay productive. Over time, these habits lead to better results at work and at home. Ultimately, effective time management supports both personal growth and long-term success.",
            "Healthy eating plays a key role in maintaining overall well-being. A balanced diet provides the nutrients the body needs to function properly. Fruits and vegetables are rich in vitamins and minerals that support the immune system. Whole grains offer lasting energy and help with digestion. Lean proteins are essential for building and repairing tissues. It is also important to drink enough water throughout the day. Limiting processed foods and added sugars can reduce the risk of many health problems. By making small, consistent changes, individuals can develop eating habits that benefit them for years to come.",
            "Remote work has become increasingly common in recent years. Many organizations have adopted flexible arrangements to support their employees. Working from home can reduce commuting time and improve work-life balance. However, it also presents challenges such as isolation and distractions. Clear communication is essential for remote teams to stay aligned. Digital tools make it easier to collaborate across different locations. Managers play an important role in keeping employees engaged and motivated. Overall, remote work offers significant benefits when it is supported by the right strategies, tools, and organizational culture.",
            "Reading regularly offers many benefits for people of all ages. It helps to expand vocabulary and improve communication skills. Reading also strengthens concentration and memory over time. Through books, individuals can learn about new cultures, ideas, and perspectives. Fiction in particular can build empathy by allowing readers to experience different lives. In addition, reading before bed can be a relaxing way to reduce stress. Libraries and digital platforms make books more accessible than ever before. By making reading a daily habit, people can enjoy both personal enrichment and lifelong learning.",
            "Exercise is an essential part of a healthy lifestyle. Regular physical activity strengthens the heart and improves circulation. It also helps to maintain a healthy weight and build muscle strength. Exercise has important mental health benefits as well, including reduced anxiety and improved mood. Even simple activities such as walking or stretching can make a meaningful difference. It is important to choose activities that are enjoyable so that they become a consistent routine. Setting realistic goals can help individuals stay motivated. In the long run, regular exercise contributes to a longer, healthier, and more active life.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # One text for each label, taken from my unit 7 tests.
        "texts": [
            # human: my Cozy Tap Club blurb (scored 0.1258 in unit 7)
            "Welcome to Cozy Tap Club. Satisfying mobile gameplay with a story on top. I play cooking games, sorting games, brain puzzles, and cozy builders like Township and Gossip Harbor, sometimes paired with a story to keep you hooked till the last level.",
            # unsure: AI-style paragraph (scored 0.6848 in unit 7)
            "In the modern world, it is important to understand that effective communication plays a crucial role in achieving success. By leveraging key strategies and best practices, individuals can enhance their productivity. Furthermore, it is essential to recognize the importance of continuous improvement. Ultimately, a consistent approach leads to meaningful and lasting results.",
            # ai: evenly sized sentences (scored 0.8017 in unit 7)
            "Effective communication is an important skill in the workplace today. It helps teams share ideas and solve problems together. Strong communication also improves productivity and builds trust. Organizations that value communication achieve better results over time.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # The five inputs named in criterion 5. Each should get a 400.
        "bodies": [
            {"creator_id": "eval_bad_no_text"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "     ", "creator_id": "eval_bad_spaces"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": "This is a normal sentence with no creator id attached to it."},
        ],
    },
    # Criterion 4 (the appeal path) is tested by hand with check_appeals.py,
    # because it needs a submission first and then an appeal on its content_id.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
