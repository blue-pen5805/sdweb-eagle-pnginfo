import re
from modules import prompt_parser, shared, extra_networks

class Parser:
    def prompt_to_tags(prompt):
        use_prompt_parser = shared.opts.use_prompt_parser_when_save_prompt_to_eagle_as_tags
        threshold = shared.opts.save_tags_words_threshold

        p, _ = extra_networks.parse_prompt(prompt)
        if use_prompt_parser:
            p = ','.join(map(lambda x: x[0].strip(), prompt_parser.parse_prompt_attention(p)))

        tags = [ x.strip() for x in p.split(",") if x.strip() != "" ]
        if threshold > 0:
            tags = list(filter(lambda x: len(x.split(" ")) < threshold, tags))

        return tags

    def extra_networks_to_tags(prompt):
        tags = []
        for match in re.finditer(extra_networks.re_extra_net, prompt):
            tags.append(match.group())

        return tags
