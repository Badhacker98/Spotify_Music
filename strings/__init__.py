import os
from typing import List

import yaml

LOGGERS = "Gaana_MusicBot"

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]

# Load English commands first and set English keys
commands["en"] = load_yaml_file(r"./strings/cmds/en.yml")
english_keys = set(commands["en"].keys())

for filename in os.listdir(r"./strings/cmds/"):
    if filename.endswith(".yml") and filename != "en.yml":
        language_code = filename[:-4]
        commands[language_code] = load_yaml_file(
            os.path.join(r"./strings/cmds/", filename)
        )

        missing_keys = english_keys - set(commands[language_code].keys())
        if missing_keys:
            print(
                f"Error: Missing keys in strings/cmds/{language_code}.yml: {', '.join(missing_keys)}"
            )
            sys.exit(1)

for filename in os.listdir(r"./strings/helpers/"):
    if filename.endswith(".yml"):
        language_code = filename[:-4]
        helpers[language_code] = load_yaml_file(
            os.path.join(r"./strings/helpers/", filename)
        )

if "en" not in languages:
    languages["en"] = load_yaml_file(r"./strings/langs/en.yml")
    languages_present["en"] = languages["en"]["name"]

for filename in os.listdir(r"./strings/langs/"):
    if filename.endswith(".yml") and filename != "en.yml":
        language_name = filename[:-4]
        languages[language_name] = load_yaml_file(
            os.path.join(r"./strings/langs/", filename)
        )

        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]

        try:
            languages_present[language_name] = languages[language_name]["name"]
        except KeyError:
            print(
                "There is an issue with the language file. Please report it to TheTeamvk at @TheTeamvk on Telegram"
            )
            sys.exit()

if not commands:
    print(
        "There's a problem loading the command files. Please report it to TheTeamVivek at @TheTeamVivek on Telegram"
    )
    sys.exit()


def command(
    commands: Union[str, List[str]],
    prefixes: Union[str, List[str], None] = "/",
    case_sensitive: bool = False,
):
    async def func(flt, client: Client, message: Message):
        lang_code = await get_lang(message.chat.id)

        if isinstance(commands, str):
            commands_list = [commands]
        else:
            commands_list = commands
            

for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()
      
