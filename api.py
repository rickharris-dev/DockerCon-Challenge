import subprocess
from subprocess import Popen, PIPE
from flask import Flask

app = Flask(__name__)

@app.route("/<image>")

def command(image, git_repo_url):
    print "running command..."
    result = run_commands(image, git_repo_url)
    return result


@app.route("/test/")
def neat():
    return "This works!"


def pull_github(git_repo_url):



def run_commands(image):

    container_id = "GAUNTLET"
    # initiate container command
    make_container = [
        "docker",
        "run",
        "-v",
        "/Users/Icarus/docker_test/the-gauntlet/:/tmp/",
        "--name",
        container_id,
        "-dit",
        image,
    ]

    # compile command
    compile_file = [
        "docker",
        "exec",
        container_id, #specify container id to be used
        "gcc", #specify command to run
        "/tmp/test.c", #specify file to run command with
        "-o",
        "/tmp/HERE",
    ]

    # execution command
    execute_file = [
        "docker",
        "exec",
        container_id, #specify container id to be used
        "/tmp/HERE"
    ]

    # stop container
    stop_container = [
        "docker",
        "stop",
        container_id
    ]

    # remove container
    rm_container = [
        "docker",
        "rm",
        container_id
    ]

    # clone repo
    clone_repo = [
        "docker",
        "exec",
        container_id,
        "git",
        "clone",
        git_repo_url
    ]

    # create docker container
    print "creating docker container..."
    proc = subprocess.Popen(make_container, stdout=PIPE, stderr=PIPE)
    res, stderr = proc.communicate()

    # clone repo
    proc = subprocess.Popen(make_container, stdout=PIPE, stderr=PIPE)
    print "Cloned! (unless error...)"

    # try to compile
    print "attempting to compile"
    proc = subprocess.Popen(compile_file, stdout=subprocess.PIPE)
    err = proc.stdout.read()
    res = err

    if err:
        proc = subprocess.Popen(stop_container, stdout=subprocess.PIPE)
        proc = subprocess.Popen(rm_container, stdout=subprocess.PIPE)
        return "Output is (error): " + err

    # try to execute
    else:
        proc = subprocess.Popen(execute_file, stdout=subprocess.PIPE)
        res = proc.stdout.read()

        proc = subprocess.Popen(stop_container, stdout=subprocess.PIPE)
        proc = subprocess.Popen(rm_container, stdout=subprocess.PIPE)
        return "Output is: " + res

# response_body = {
#     status: 1,
#     stdin: compile_file,
#     stdout: err,
#     stderr:
# }
# send response of int 1 and err


# response = {
#     status: int,
#     stdin: stdin,
#     stdout: stdout,
#     stderr: stderr
# }


if __name__ == "__main__":
    app.run()
