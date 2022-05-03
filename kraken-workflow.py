def stage(ctx):
    langs = [
        ('C', 'gcc:11.3'),
        ('C++', 'gcc:11.3'),
        ('C#', 'mono:6.12'),
        ('Clojure', 'clojure:1.11'),
        ('Elixir', 'elixir:1.13'),
        ('Erlang', 'erlang:23.3'),
        ('Go', 'golang:1.18'),
        ('Groovy', 'groovy:3.0'),
        ('Haskell', 'haskell:9.2'),
        ('Haxe', 'haxe:4.2'),
        ('Java', 'openjdk:11'),
        ('Julia', 'julia:1.7'),
        ('Perl', 'perl:5.34'),
        ('PHP', 'php:8.0'),
        ('Python', 'python:3.8'),
        ('Rust', 'rust:1.60'),
        ('Ruby', 'ruby:3.1'),
        ('Swift', 'swift:5.6'),
    ]

    jobs = []

    for lang_name, lang_image in langs:
        jobs.append({
            "name": "hello world %s" % lang_name,
            "steps": [{
            "tool": "git",
                "checkout": "https://github.com/Kraken-CI/hello-worlds.git",
                "branch": "main"
            }, {
                "tool": "shell",
                "script": """
                    wget https://github.com/sharkdp/bat/releases/download/v0.20.0/bat-v0.20.0-x86_64-unknown-linux-gnu.tar.gz
                    tar -zxvf bat-v0.20.0-x86_64-unknown-linux-gnu.tar.gz
                    chmod a+x bat-v0.20.0-x86_64-unknown-linux-gnu/bat
                    sudo mv bat-v0.20.0-x86_64-unknown-linux-gnu/bat /usr/bin
                    echo '#/bin/bash\nbat --color always $1' > cat.sh
                    chmod a+x cat.sh
                    sudo mv cat.sh /usr/bin/cat
                """
            }, {
                "tool": "shell",
                "cmd": "./run.sh %s" % lang_name,
                "cwd": "hello-worlds"
            }],
            "environments": [{
                "executor": "docker",
                "system": "krakenci/%s" % lang_image,
                "agents_group": "all",
                "config": "default"
            }]
        })

    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": jobs
    }
