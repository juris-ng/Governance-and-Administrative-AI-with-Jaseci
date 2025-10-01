node democracy_platform {
    has platform_name: str = "Next-Gen Local Democracy";
    has active_users: int = 0;
}

with entry {
    print("??? DEMOCRACY PLATFORM DEMO");
    print("========================");
    platform = spawn democracy_platform();
    platform.active_users = 3;
    print("Platform: " + platform.platform_name);
    print("Active users: " + str(platform.active_users));
    print("? Democracy platform is operational!");
}
