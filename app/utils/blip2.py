from PIL import Image
from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch
import os
import openai

class ImageToLanguage():
    def __init__(self) -> None:
        self.processor=AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
        self.model=Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")
        self.device="cuda" if torch.cuda.is_available() else "cpu"
    def get_text(self,image):
        self.model.to(self.device)
        inputs = self.processor(image, return_tensors="pt").to(self.device)
        generated_ids = self.model.generate(**inputs, max_new_tokens=20)
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
        messages = [{"role":"user","content":"将下面的句子翻译成中文："+generated_text}]
        openai.api_key = os.getenv("OPENAI")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chat_response = completion
        answer = chat_response.choices[0].message.content
        return answer
    
if __name__=='__main__':
    imageToLanguage=ImageToLanguage() 
    # 调用类方法传入一张图片
    image = Image.open('1.jpg').convert('RGB')
    answer=imageToLanguage.get_text(image) 
    # TODO：将answer包装成结果返回前端