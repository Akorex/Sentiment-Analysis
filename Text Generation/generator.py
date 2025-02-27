"""This is the python file accompanying the notebook on text generation from 
scratch with HuggingFace
"""

from transformers import AutoTokenizer, TFGPT2LMHeadModel, pipeline, AutoConfig

tokenizer = AutoTokenizer.from_pretrained('gpt2')
config = AutoConfig.from_pretrained('gpt2', vocab_size=len(tokenizer), 
                                    bos_token_id=tokenizer.bos_token_id,eos_token_id=tokenizer.eos_token_id, n_ctx=128)


checkpoint = 'path_to_checkpoint'

model = TFGPT2LMHeadModel(config)
model(model.dummy_inputs) # build the model
model.load_weights(checkpoint) # load the weights trained


def generate_text(text):
    """Loads the model and generate text 

    Args:

        checkpoint: path to the model saved  
    """
    pipe = pipeline("text-generation", model= model, tokenizer=tokenizer, device=0)

    output = pipe(text)[0]['generated_text']

    return output