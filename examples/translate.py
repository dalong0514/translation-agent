import os, time

import translation_agent as ta
import common_tools as common_tools

if __name__ == "__main__":
    source_lang, target_lang, country = "English", "Chinese", "China"

    full_path = '/Users/Daglas/Desktop/input.md'

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    start_time = time.time()
    print('waiting...\n')

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    translation = common_tools.modify_text(translation)
    common_tools.write_file('/Users/Daglas/Desktop/output.md', translation)

    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')
