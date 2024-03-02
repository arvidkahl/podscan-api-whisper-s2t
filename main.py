import whisper_s2t
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--initial_prompt', type=str, help='Initial prompt for the Whisper S2T model')
parser.add_argument('--file', type=str, help='File path')
parser.add_argument('--model', type=str, help='The model to use')

args = parser.parse_args()

model = whisper_s2t.load_model(model_identifier=args.model, backend='CTranslate2')

files = [args.file]
lang_codes = ['en']
tasks = ['transcribe']
initial_prompts = [args.initial_prompt]

out = model.transcribe_with_vad(files,
                                lang_codes=lang_codes,
                                tasks=tasks,
                                initial_prompts=initial_prompts,
                                batch_size=48
                                )
whisper_s2t.write_outputs(out, format='txt', ip_files=files, save_dir="./") # Save outputs