import gymnasium as gym

from .env import WebshopEnv  # noqa
from .model import HumanPolicy, OpenAIPolicy  # noqa

if __name__ == "__main__":
    env = gym.make("Webshop-v0")
    observation, info = env.reset()
    persona = """
Persona: Clara
Background:
Clara is a PhD student in Computer Science at a prestigious university. She is deeply engaged in research focusing on artificial intelligence and machine learning, aiming to contribute to advancements in technology that can benefit society.

Demographics:

Age: 28
Gender: Female
Education: Pursuing a PhD in Computer Science
Professional Life:
Clara spends most of her time in academia, attending conferences, working in the lab, and writing papers. Her commitment to her research is her main priority, and she manages her time around her academic responsibilities.

Financial Situation:
Clara have a rich family, so she cares quality of the goods more than the price.

Shopping Habits:
Clara dislikes shopping and avoids spending much time browsing through products. She prefers straightforward, efficient shopping experiences and often shops online for convenience. When she does shop, she looks for practicality and affordability over style or trendiness.

Personal Style:
Clara prefers comfortable, functional clothing, often choosing items that are easy to wear for long hours spent at her desk or in the lab. She wears XXL-sized clothing and likes colors that reflect her personality—mostly grey, which she finds uplifting and energizing.
"""

    try:
        policy = OpenAIPolicy(persona, "buy a faux jacket")

        while True:
            print(observation["url"])
            clickables = observation["clickables"]
            print("clickables:", clickables)
            action = policy.forward(observation, clickables)
            observation, reward, terminated, truncated, info = env.step(action)
            print(f'Taking action "{action}" -> Reward = {reward}')
            print("-" * 50)
            if terminated:
                break
    finally:
        env.close()
        import json

        print(json.dumps(policy.short_term_memory, indent=2))
        print(json.dumps(policy.previous_actions, indent=2))
