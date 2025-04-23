#communcating with llm with a given prompt I used TinyLLama due to hugging face token issues and it is still powerful and most importantly -- free

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0", device_map="auto", torch_dtype="auto")

llm = pipeline("text-generation", model=model, tokenizer=tokenizer)

def genereate_summary(news_list, user_instruction):
    prompt = user_instruction + "\n\nHere is what reputable financial news outlets are saying:\n" + "\n".join(news_list)
    out = llm(prompt, max_new_tokens=150, do_sample=True)
    return out[0]['generated_text']
