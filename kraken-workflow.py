def stage(ctx):
    langs = [
        ('C', 'gcc:11.3'),
        ('C++', 'gcc:11.3'),
        ('C#', 'mono:6.12'),
        ('Clojure', 'clojure:1.11'),
        ('Elixir', 'elixir:1.13'),
        ('Erlang', 'erlang:23.3'),
        ('Go', 'golang:1.18'),
        ('Java', 'openjdk:11'),
        ('Python', 'python:3.8'),
        ('Rust', 'rust:1.60'),
        ('Ruby', '3.1'),
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
