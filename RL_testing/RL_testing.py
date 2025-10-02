import gymnasium as gym
import keyboard
import time

def manual_control_loop(env):
    """Цикл для ручного управления."""
    print("\nУправление начато. Используйте клавиши 'влево' и 'вправо'. Закройте окно для выхода.")
    total_reward = 0
    observation, info = env.reset()
    
    while True:
        try:
            env.render()
            action = 0  # По умолчанию - влево
            if keyboard.is_pressed('right'):
                action = 1

            observation, reward, terminated, truncated, info = env.step(action)
            total_reward += reward

            if terminated or truncated:
                print(f"Эпизод завершен! Общая награда: {total_reward}")
                total_reward = 0
                observation, info = env.reset()

            time.sleep(0.01)

        except gym.error.ClosedEnvironmentError:
            print("\nОкно симуляции закрыто. Программа завершена.")
            break

def default_control_loop(env):
    """Цикл для автоматического (случайного) управления."""
    print("\nАвтоматическое управление начато. Закройте окно для выхода.")
    total_reward = 0
    observation, info = env.reset()

    while True:
        try:

            env.render()
            
            action = env.action_space.sample()
            
            observation, reward, terminated, truncated, info = env.step(action)
            total_reward += reward

            if terminated or truncated:
                print(f"Эпизод завершен! Общая награда: {total_reward}")
                total_reward = 0
                observation, info = env.reset()

        except gym.error.ClosedEnvironmentError:
            print("\nОкно симуляции закрыто. Программа завершена.")
            break


def main():
    """Основная функция для выбора режима и запуска симуляции."""

    env = gym.make("CartPole-v1", render_mode="human")

    while True:
        mode = input("Выберите режим управления ('manual' или 'default'): ").lower().strip()
        if mode in ["manual", "default"]:
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'manual' или 'default'.")

    if mode == "manual" or "m":
        manual_control_loop(env)
    else:
        default_control_loop(env)

    env.close()

if __name__ == "__main__":
    main()