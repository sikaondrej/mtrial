for file_name in sorted(os.listdir(normpath(PROJECT_ROOT, "ext"))):
    if "_" in file_name and not "__" in file_name:
        execfile(normpath(PROJECT_ROOT, "ext", file_name, "conf/settings.py"))
        sys.path.append(normpath(PROJECT_ROOT, "ext", file_name))
        INSTALLED_APPS.append("ext."+file_name)
