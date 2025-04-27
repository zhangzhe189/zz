from openai import OpenAI
import time

def new_chat(api_key, stream=True, base_url="https://api.deepseek.com/"):

    client = OpenAI(api_key=api_key, base_url=base_url)
    messagesData = []

    print("请输入内容，与 deepseek 聊天（输入 \"结束对话\"退出）")

    while True:
        user_input = input("我: ")

        if user_input == "结束对话":
            print("deepseek: 再见!")
            break

        messagesData.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messagesData,
                stream=stream,
            )

            if stream:
                deepseek_reply = ""
                print("deepseek: ", end="", flush=True)
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        word = chunk.choices[0].delta.content
                        print(word, end="", flush=True)
                        deepseek_reply += word
                        time.sleep(0.1)
                print() 
            else:
                deepseek_reply = response.choices[0].message.content.strip()
                print(f"deepseek: {deepseek_reply}")

            if deepseek_reply:
                messagesData.append({"role": "assistant", "content": deepseek_reply})
            else:
                print("deepseek: 请稍后再试。")

        except Exception as e:
            print(f"deepseek: 请求失败，错误信息：{e}")

if __name__ == "__main__":
    API_KEY = "sk-80c4176ffedb478aa3ed7fbaae196486"
    new_chat(api_key=API_KEY, stream=True)
