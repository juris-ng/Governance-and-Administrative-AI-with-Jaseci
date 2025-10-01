node democracy_platform {
    has platform_name: str = "Next-Gen Local Democracy";
}

walker init_platform {
    can setup with entry {
        print("Starting democracy platform...");
        platform = spawn democracy_platform();
        print("Platform created successfully!");
        print("Platform name:", platform.platform_name);
    }
}