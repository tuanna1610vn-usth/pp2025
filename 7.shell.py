import subprocess
import shlex

def main():
    while True:
        try:
            command = input("shell> ")
            if command.lower() == "exit":
                break
            
            # Pipe creating: Process A -> Pipe -> Process B
            if "|" in command:
                # Splitting processes from user input
                commands = []
                cmd = command.split("|")
                for c in cmd:
                    commands.append(shlex.split(c.strip()))

                prevProcess = None
                for c in commands:
                    if prevProcess == None:
                        process = subprocess.Popen(c, stdout=subprocess.PIPE)
                    else:
                        process = subprocess.Popen(c, stdin=prevProcess.stdout, stdout=subprocess.PIPE)
                        prevProcess.stdout.close() # Previous process stop waiting for data
                    prevProcess = process
                output, _ = process.communicate()
                print(output.decode("utf-8"))

            elif ">" in command:
                cmd, outFile = command.split(">", 1)
                cmd = shlex.split(cmd.strip())
                outFile = outFile.strip()
                try:
                    output = subprocess.check_output(cmd, shell=True)
                    with open(outFile, "w") as f:
                        f.write(output.decode("utf-8"))
                except subprocess.CalledProcessError as e:
                    print(f"Command failed with return code {e.returncode}")
            
            elif "<" in command:
                cmd, inFile = command.split("<", 1)
                cmd = shlex.split(cmd.strip())
                inFile = inFile.strip()
                try:
                    with open(inFile, "r") as f:
                        process = subprocess.run(cmd, stdin=f, capture_output=True, text=True)
                        print(process.stdout, process.stderr)
                except FileNotFoundError as e:
                    print(e)
            
            else:
                subprocess.run(shlex.split(command))

        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    main()