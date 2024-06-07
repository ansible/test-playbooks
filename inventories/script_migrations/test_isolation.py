#!/usr/bin/env python3
import os
import json
import re

errors = list()

# assert that only one awx_\w*_\w* tempfile is visible
awx_tmp_files = []
for tmpdir in ("/tmp", "/var/tmp"):
    for file in os.listdir(tmpdir):
        awx_matches = re.search(r"awx_\w*_\w*", file)
        di_matches = re.search(r"runner_di_\w*", file)
        pi_matches = re.search(r"ansible_runner_pi_\w*", file)
        if awx_matches or di_matches or pi_matches:
            full_path = os.path.join(tmpdir, file)
            awx_tmp_files.append(full_path)

if len(awx_tmp_files) > 1:
    # we would see one file -- the job directory created for this job
    errors.append(("Tower temporary files", awx_tmp_files))

# assert that no project directories are visible
for tower_projects_dir in ("/var/lib/awx/projects", "/var/lib/tower/projects"):
    if not os.path.isdir(tower_projects_dir):
        continue
    files = os.listdir(tower_projects_dir)
    if files:
        files = [os.path.join(tower_projects_dir, f) for f in files]
        errors.append(("Tower project directories", files))

# assert that no job_status files are visible
for tower_job_status_dir in ("/var/lib/awx/job_status", "/var/lib/tower/job_status"):
    if not os.path.isdir(tower_job_status_dir):
        continue
    files = os.listdir(tower_job_status_dir)
    if files:
        files = [os.path.join(tower_job_status_dir, f) for f in files]
        errors.append(("Tower job_status files", files))

# assert that no tower conf files are visible
for tower_conf_dir in ("/etc/awx", "/etc/tower"):
    if not os.path.isdir(tower_conf_dir):
        continue
    files = os.listdir(tower_conf_dir)
    if files:
        files = [os.path.join(tower_conf_dir, f) for f in files]
        errors.append(("Tower config files", files))

# assert that no tower log files are visible
for tower_log_dir in ("/var/log/awx", "/var/log/tower"):
    if not os.path.isdir(tower_log_dir):
        continue
    files = os.listdir(tower_log_dir)
    if files:
        files = [os.path.join(tower_log_dir, f) for f in files]
        errors.append(("Tower log files", files))

if errors:
    err_str = "The following errors were detected while running a proot-enabled inventory_update.\\n"
    for (name, files) in errors:
        err_str += "\\n# %s\\n" % name
        err_str += " - %s" % "\\n - ".join(files)

    raise Exception(err_str)

print(json.dumps({}))
