import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

observation, info = env.reset(seed=42)
env.action_space.seed(42)
total_reward = 0

for _ in range(200):

    time.sleep(0.05)

    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    total_reward += reward

    print(f"Действие: {action}, Награда за шаг: {reward}, Суммарная награда: {total_reward}")

    if terminated or truncated:
        print("\nЭпизод завершен!")
        break

env.close()
print(f"Итоговая награда за весь эпизод: {total_reward}")