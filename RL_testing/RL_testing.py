import gymnasium as gym
import keyboard
import time

env = gym.make("CartPole-v1", render_mode="human")

observation, info = env.reset()


print(f"Начальное наблюдение: {observation}")
# [позиция_тележки, скорость_тележки, угол_шеста, угловая_скорость_шеста]

episode_over = False
total_reward = 0

print("\nУправляйте тележкой с помощью клавиш 'влево' и 'вправо'.")

while not episode_over:
    # Выбираем действие на основе нажатия клавиш
    action = 0  # По умолчанию двигаемся влево
    if keyboard.is_pressed('right'):
        action = 1  # Двигаемся вправо
    elif keyboard.is_pressed('left'):
        action = 0  # Двигаемся влево

    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    episode_over = terminated or truncated

    time.sleep(0.01)


print(f"Эпизод завершен! Общая награда: {total_reward}")
env.close()