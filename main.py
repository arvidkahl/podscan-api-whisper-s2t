import whisper_s2t
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--initial_prompt', type=str, help='Initial prompt for the Whisper S2T model')
parser.add_argument('--file', type=str, help='File path')
parser.add_argument('--model', type=str, help='The model to use')
parser.add_argument('--device', type=str, help='The device to use', default='cuda')
parser.add_argument('--compute_type', type=str, help='The compute_type to use', default='float16')
parser.add_argument('--batch_size', type=int, help='The batch size to use', default=16)

args = parser.parse_args()

model = whisper_s2t.load_model(
    model_identifier=args.model,
    backend='CTranslate2',
    device=args.device,
    compute_type=args.compute_type
)

files = [args.file]
lang_codes = ['en']
tasks = ['transcribe']
initial_prompts = [args.initial_prompt]

out = model.transcribe_with_vad(files,
                                lang_codes=lang_codes,
                                tasks=tasks,
                                initial_prompts=initial_prompts,
                                batch_size=args.batch_size
                                )
whisper_s2t.write_outputs(out, format='txt', ip_files=files, save_dir="./")