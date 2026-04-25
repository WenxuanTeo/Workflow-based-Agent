def run_workflow(steps, executor, memory, max_steps=5):
    for i, step in enumerate(steps):
        if i >= max_steps:
            break

        result = executor(step, memory.get())
        memory.add(result)

    return memory.get()
