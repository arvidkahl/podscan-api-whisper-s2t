import os

import whisper_s2t
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--initial_prompt', type=str, help='Initial prompt for the Whisper S2T model')
parser.add_argument('--file', type=str, help='File path')
parser.add_argument('--model', type=str, help='The model to use')

args = parser.parse_args()

files = [args.file]
lang_codes = ['en']
tasks = ['transcribe']
initial_prompts = [args.initial_prompt]

# create a new file

content = """[00:00.040 --> 00:13.560]: Welcome to the Bootstrap founder. I have a not so hyped yet AI topic for you today. We live in a day and age where using AI on our own servers has become possible, and I think that is magnificent. I will explain to you why.

[00:13.920 --> 00:32.920]: As a business owner and a software entrepreneur, I think that it's just as interesting as it is important to consider setting up systems on our own backends instead of relying on hosted platforms and APIs. That's just platform risk, right? And up until now, AI has been one of those things that you only get on somebody else's platform.

[00:33.560 --> 00:57.020]: If you're a software founder interested in using AI technology without depending on someone else's unit economics, this is for you today. We'll dive into running your own chat GPT replacement for fun and more importantly, I guess, for profit. I've been tinkering with this kind of tech over the last couple weeks to great success. So in the spirit of building in public, why not tell you what and how I did?

[00:57.760 --> 01:24.200]: In my latest SaaS pod scan I use two kinds of artificial intelligence. The first one is an audio to text transcription system called Whisper and there's an LLM, a large language model like ChatGPT that generates responses based on prompts. The transcription system is pretty cool but it's not something that every software entrepreneur needs because it's really specific to converting audio into text and audio is a niche medium for most of us but

[01:24.400 --> 01:52.880]: I would say all software founders work with text data in some shape or form. Some more in a database, right? Customer records, notes, instructions, it's all text. And founders got very excited back in the day when chat GPT came out, which now I guess is two years ago, which in terms of our industry is really just a blip, right? But still people got super excited. All of a sudden, particularly once we could access that kind of service through an API, we could build on top of these amazingly smart language models.

[01:52.960 --> 02:21.140]: And that pioneering spirit has brought us to an interesting inflection point. Because the open in OpenAI, the company that spearheaded the whole chat GPT and all the GPT systems, that has been a catalyst for the open source community as well. It turns out that the most exciting development in recent years is not just the existence of the GPTs and chat GPT, but the fact that many universities, research groups and companies have open sourced their code for training and running these models.

[02:21.040 --> 02:31.500]: And when the nerds start building stuff together in the open, working on public data, working in public building in public for free and without restrictions, interesting things start to happen.

[02:31.120 --> 02:51.840]: And one of them is called llama.cpp. That's L L A M A dot cpp I guess. It is a cross platform framework that I found that is completely open source that allows us to train and run our own AI models on our consumer hardware that we own. Our computers, our laptops, our desktop systems, our servers if we want to.

[02:51.460 --> 03:08.060]: And we don't need to have the massive GPUs and RAM amounts that the big guys have, but we still get to run tech that's almost as good. Obviously if you have GPUs that have hundreds of gigabytes of RAM, you can run larger models, which is what GPT is.

[03:08.060 --> 03:31.300]: tens if not hundreds of billions of parameters that they're trained on, the models that run on consumer hardware, they have seven or maybe 13 billions of parameters, which is still a lot of parameters. But you know, it's just a slight difference there. But again, almost as good. And in most cases, for entrepreneurs, particularly when you're starting out building prototypes and stuff, it's good enough.

[03:31.620 --> 03:51.120]: The big contributor here is that we can avoid those costs and dependencies associated with using hosted platforms like OpenAI's API. And in addition to that, or maybe because of it, we gain more control and flexibility over AI applications for our own businesses. So the risk goes down and control goes up.

[03:50.860 --> 04:08.100]: And that kind of is the indie founder's dream, right? You de-risk and you get more control. I think that's just wonderful. Let me share an example from just this week that I have found worked to work really well with my own business. Podscan was, until Wednesday, a keyword alerting tool for podcasts.

[04:08.480 --> 04:28.160]: You would write down or configure a list of words in my user interface and Podstan would transcribe every newly released podcast out there as quickly as it could, then compare your list against the transcript and alert you if there was a match. Just regular kind of keyword matching. The magic in this product really is that it ingests all podcasts everywhere, but

[04:28.160 --> 04:40.880]: It was a fairly simple kind of checking for keywords. So far, so good. And this is already creating massive value in the world of podcast discovery, which is severely underserved and it's kind of hard because audio is hard to introspect.

[04:40.740 --> 05:06.260]: But, now consider this from a user perspective. What if you don't know the keywords beforehand? What if you want to be alerted for something that is more nebulous? Something like all podcasts where people talk about community events that are organized by women or all podcasts where people really nerd out about their favorite TV show. You can't just look for TV show as a keyword. That's just going to give you everybody talking about every TV show in any capacity.

[05:06.940 --> 05:23.340]: And even if you wanted to you couldn't come up with all the specific keywords that would allow you to reliably match every podcast that falls into these categories either but what if you could ask a simple question to each show questions like dust this episode have nerds talk about sci fi in an excited way.

[05:23.660 --> 05:51.320]: And that's what local AI allowed me to build in like a day and a half, which is crazy. With the help of llama.cpp and a large language model called Mistral 7b, the 7b should not be surprising. I just mentioned that some of these models have 7 billion parameters. I set up a backend service that takes a transcript that the other AI in my system creates. It takes a question and then it spits out either a yes or a no.

[05:52.260 --> 06:11.000]: And that means that if the question is answered with a yes, is this a show hosted by nerds t
alking about sci-fi, then you get an alert. But only then. And this system takes any transcript and any question and an
swers the question on that transcript in under a second per combination.

[06:11.540 --> 06:28.080]: And most importantly, it does this on the same hardware that my transcription servers are al
ready running on. And they're just like gobbling up all these new podcast episodes and transcribing them. In between tr
anscriptions, I sometimes just do some inference, right? Ask this question of the transcript.

[06:28.420 --> 06:50.220]: I don't have to count API calls. I just have to have a computer with a GPU with like 8GB of
RAM, a little bit more maybe, but that is enough. And cloud hosting for GPUs right now is still super expensive. You pa
y around $500 per month for a single server with a GPU. But even Mac Mini, which is like $800, can run this kind of AI
inference at one question.

[06:50.440 --> 07:15.300]: to a transcript per second. And it's quite literally both what I'm recording this on right n
ow and where it's running in the background still. Like I'm recording a podcast episode on the computer that is just in
ferring and transcribing as I speak. That's the power of GPU based stuff, right? The GPU is not needed for audio record
ing so it can just pull in data and deal with audio while I speak. It's incredible.

[07:15.300 --> 07:35.920]: And platforms like OpenAI and other competitors have started to compete there on price. They
 understand that people have started to run this locally too. OpenAI's API is a big mover here towards lower prices. It
's really, really affordable to use GPD 3.5. It's kind of the budget version of GPD because the current GPD

[07:35.920 --> 08:02.360]: most recent version is GPT-4 and it's super powerful, has a much more recent knowledge cutof
f and it's more performant in certain things. And GPT-3.5 is kind of what we had when we started out-ish, right? It's g
ood for any task that you need to scale on. And you can get millions of tokens, and those are words or characters, for
under a dollar. That's quite impressive, and let's be reasonable. I guess it fits most budgets if you just have to work
 through some text data some of the time.

[08:02.360 --> 08:26.280]: But it doesn't fit all budgets. If you deal with lots of data, then you need to run prompts
on the data constantly. Like if you were analyzing every English speaking podcast out there at all times, GPD 3.5 can c
ost tens, we have hundreds of dollars per day. GPD 4 would easily go into the thousands if you were running it constant
ly. That's not scalable for a small business. But running your own local LLM? That sure is.

[08:26.060 --> 08:49.360]: Having AI on a server was impossible for a long time and the requirement of current GPUs sti
ll makes it somewhat expensive. But fortunately, AI comes in two forms, inference and training. The inference is applyi
ng a prompt and getting a reply and training is setting up the model. And inference itself is surprisingly possible on
regular old CPUs as well.

[08:49.700 --> 09:12.080]: Traditionally, over the last few years, all kinds of machine learning and AI work has been d
one on a GPU, because GPUs are designed for massive parallel computation. They're graphics processing. They are suppose
d to create these really immersive game worlds. And recent CPUs have added TensorCores, which handle specific mathemati
cal operations that are also used in games and machine learnings and all kinds of other computation-heavy things.

[09:12.080 --> 09:23.280]: So your computer's boring old CPU handles regular, more straightforward linear computations
and the GPU is much faster for certain parallel tasks. But in recent times,

[09:23.820 --> 09:49.400]: LLMs that used to require a GPU now run hilariously fast on a CPU as well, mostly also becau
se those CPUs have lots of cores. I recently rented a cloud server somewhere for I think it has a GPU attached. So that
's the reason why I rented but it has 32 CPU cores that I can use for CPU computation as well. It's crazy. I had the am
ount of cores that you can do parallel processing on just shot

[09:49.600 --> 10:15.640]: up magnificently so you can now do inference on those systems as well. You can run models, 7
B, 13B models even on your computer without a graphics card. And that's what most servers are, right? They are computer
 without GPUs but with quite some RAM and a lot of CPU cores in there as well. And this change has led to the growth of
 an open source community creating local launch language model tools that can be used on both kind of chips.

[10:15.340 --> 10:34.600]: And that's the .cpp in llama.cpp. It's C++. It signifies that these tools were meant for CPU
-based inference. And WhisperCPP, the Speech-to-Text sibling project, also is meant to run on a CPU. And the open sourc
e nature of these projects has been supported by an unlikely ally.

[10:34.840 --> 11:00.800]: Meta, the company behind Facebook, the company we all love for their privacy intrusion and t
hat kind of stuff, they released an open source large language model called Llama in 2023. And that's pretty big for th
em to go into open source that much. I mean, they've done this with React and other projects, but you know, it is prett
y significant that the competitor, the OpenAI's competitor, that would be Meta, releases their models and their trainin
g data and all that for free.

[11:01.340 --> 11:22.920]: Because OpenAI's GPT models are proprietary. The company has published only research papers,
 no code. That inspired people to build their own models using public data. There's even a benchmarking system to compa
re these self-trained models like Mistral 7b and all these many many others with the proprietary models like GPT-3 or G
PT-4. And some of these new models come pretty close.

[11:22.540 --> 11:49.980]: Now, independent companies and open source communities release new large language models dai
ly now that perform better than GPD 3.5. Maybe not as scalable, they don't have the infrastructure that OpenAI has with
 their whole server cluster, but the model itself performs better, more accurately and more reliably, sometimes faster.
 And these things almost perform as well as GPD 4, which is kind of the gold standard of these models right now in term
s of speed and accuracy.

[11:50.180 --> 12:15.940]: These open source models are available to everyone that includes me and includes you and the
y help advance the field of AI language processing quite significantly because the moment we start using these things w
e find the flaws, we report this on GitHub and all these pages that exist where these models are hosted. And you will f
ind those models on huggingface.co which is an interesting name for an interesting company but it's a website where you
 can download these open source language models in various forms.

[12:15.940 --> 12:38.440]: whatever form you need, whatever tool you use, you will find the model of your choice in tha
t format there. I recommend following a person called Tom job in there. I think their nickname is the bloke. Tom's mode
ls come in all kinds of formats and they've been reliably good to me. I've been using models from that person's page th
ere quite a lot. People like Tom, they don't just get

[12:38.300 --> 13:02.400]: upload the model, share the source material, the training data and all the files needed to r
un it on your own computer, which is really cool. That's really all that is to that. You download llama.cpp from GitHub
, you compile it and it's a cross platform thing so it works on Windows, on Linux, on Mac, doesn't really matter. You d
ownload a model which is just one download from huggingface.co.

[13:02.400 --> 13:27.820]: think you even need to be logged in there to download it. And then you're done. Lama lets yo
u run a command on your computer or start a little server that loads a large language model into your graphics card mem
ory or your regular memory. And then it allows you to do local inference through an API, like HTTP, you send an HTTP re
quest, or you just put the link to the file or the link to a JSON file where you have some data in there. And it's craz
y. It even comes with an example page. It's very simple to use.

[13:28.140 --> 13:53.820]: And even if you're not into AI and don't see an immediate use for it, I highly recommend loo
king into this. Llama automatically detects the best capacity your computer has for running inference, checks if there
is a GPU available, if you have the right drivers and if you have the toolkits installed that you need, and then it use
s these to maximize efficiency. And the community on the GitHub page is really, really good too. So you will find a lot
 of help if you want to set this up. You'll have a fast

[13:53.820 --> 14:13.700]: As fast and performant, I guess, an API on your own personal computer as you would if you we
re to use an API. And that's quite magical. And it's yours. That's the thing, right? I think this is the year where sof
tware entrepreneurs learn how to wrangle control back onto their systems. And AI is one of the fields where this happen
s.

[14:13.320 --> 14:32.820]: It's going to be a wild ride for sure and things change every day, but there's something inc
redibly powerful about knowing that OpenAI can implode tomorrow and shut down the API, but my local installation of Mis
tral 7b and a couple of cloud computers that have it running too will still be mine to command.

[14:33.000 --> 14:48.060]: They don't belong to anybody but me. I mean, it's the cloud, somebody else's computer. But y
ou know what I mean, right? The installation, the software itself, something that I could clone as an image and run som
ewhere else, that is mine. Local AI is powerful, and it's here to stay.

[14:48.320 --> 15:17.700]: And that's it for today. I want to briefly thank my sponsor, acquire.com. Because one thing
that stood out to me this week as well in reflecting on this is how much more sellable having ownership over your back
end magic like AI can make your business. An acquirer always buys your liabilities as well. That's what they buy. They
buy the good and the bad. They buy the whole business. But if you have these powerful AI systems in-house on your serve
rs, their liability is kind of reduced to keeping the servers running.

[15:17.400 --> 15:30.600]: And frankly, that is what they're used to anyway. That's how acquirers work. They know that
software businesses need servers to keep running, right? So for them, the AI on the back end is a bonus.

[15:30.680 --> 15:57.040]: And local AI, therefore, is kind of an acquisition price boost for when you eventually sell
your software business. And I guess there are many reasons to sell your business. Maybe you are done. Maybe you're done
 with the work. You built what you wanted to build. You want to do something else. You reached a skill ceiling. You wan
t a different lifestyle, whatever it is. No matter why you might want a change in your life, selling your business at t
hat point is probably a very impactful and positive experience.

[15:56.840 --> 16:22.000]: Especially if you sell your SaaS on acquire.com. The folks over there, they've helped thousa
nds of people sell their valuable businesses for life-changing amounts of money. And the thing is you don't have to sel
l today. But if you're ever interested in pivoting into financial security, you probably want to check out acquire.com.
 Go to try.acquire.com slash arbit and see if this is for you and your business right now. It's always good to plan ahe
ad.

[16:22.380 --> 16:50.880]: Thank you for listening to the Boots of Founder today. You can find me on Twitter at avidcon
, A-I-V-I-D-K-A-H-L. If I buy books, I'm on Twitter across that too. If you want to support me and this show, please su
bscribe to my YouTube channel, get the podcast and your player of choice and leave a five star rating and a review by g
oing to readthispodcast.com slash founder. That makes a massive difference if you show up there because then the podcas
t will show up in other people's feeds and this will help the show. Thank you so much for listening. Have a wonderful d
ay and bye bye.

"""

directory, file_name = os.path.split(args.file)
name, ext = os.path.splitext(file_name)

# Prefix the file name with '0_' and change the extension to '.txt'
new_file_name = f"0_{name}.txt"
# Prefix the file name with '0_'
# Combine the directory and the new file name
new_file_path = os.path.join(directory, new_file_name)

file_name = f"{new_file_path}"
with open(file_name, 'w') as file:
    file.write(content)
    file.close()