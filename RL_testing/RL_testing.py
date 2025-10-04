import gymnasium as gym
import time
import keyboard

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

total_reward = 0

print("Управление запущено! Используйте стрелки <влево> и <вправо> для управления.")
print("Чтобы остановить, закройте окно симуляции.")

action = 0 

for _ in range(500):
    if keyboard.is_pressed('left'):
        action = 0  # Двигать тележку влево
        print("Нажата стрелка влево!", end='\r')
    elif keyboard.is_pressed('right'):
        action = 1  # Двигать тележку вправо
        print("Нажата стрелка вправо!", end='\r')
    
    # --- Конец блока ручного управления ---

    # Выполняем выбранное действие в среде
    observation, reward, terminated, truncated, info = env.step(action)

    total_reward += reward

    time.sleep(0.02)

    if terminated or truncated:
        print("\nЭпизод завершен!")
        break

env.close()
print(f"\nИтоговая награда за весь эпизод: {total_reward}")