def sayMessage(args) {
    println "Hello ${args.name}, ${args.message}"
}

sayMessage name: "Bob", message: "how are you?"
