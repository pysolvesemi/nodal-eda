use std::process::{Command, Output};

fn cli(args: &[&str]) -> Output {
    Command::new(env!("CARGO_BIN_EXE_nodal-eda"))
        .env_clear()
        .args(args)
        .output()
        .expect("CLI should execute without external tools or environment")
}

#[test]
fn help_is_stable_and_requires_no_environment() {
    let help = cli(&["--help"]);
    assert!(help.status.success());
    assert!(help.stderr.is_empty());
    let text = String::from_utf8(help.stdout.clone()).unwrap();
    assert!(text.contains("Usage: nodal-eda [--help | --version]"));
    assert!(text.contains("This bootstrap provides help and version commands."));
    for args in [&[][..], &["-h"][..], &["--help"][..]] {
        let result = cli(args);
        assert_eq!(result.stdout, help.stdout);
        assert!(result.status.success());
        assert!(result.stderr.is_empty());
    }
}

#[test]
fn version_has_one_machine_readable_line() {
    for arg in ["--version", "-V"] {
        let result = cli(&[arg]);
        assert!(result.status.success());
        assert_eq!(result.stdout, b"nodal-eda 0.1.0\n");
        assert!(result.stderr.is_empty());
    }
}

#[test]
fn unsupported_commands_and_extra_arguments_fail() {
    for args in [
        &["build"][..],
        &["project", "check"][..],
        &["--help", "extra"][..],
        &["--version", "--help"][..],
        &["--unknown"][..],
    ] {
        let result = cli(args);
        assert_eq!(result.status.code(), Some(2));
        assert!(result.stdout.is_empty());
        assert_eq!(result.stderr, b"error: unsupported arguments; use --help\n");
    }
}

#[cfg(unix)]
#[test]
fn non_unicode_argument_is_rejected_without_panic() {
    use std::ffi::OsString;
    use std::os::unix::ffi::OsStringExt;
    let result = Command::new(env!("CARGO_BIN_EXE_nodal-eda"))
        .env_clear()
        .arg(OsString::from_vec(vec![0xff]))
        .output()
        .unwrap();
    assert_eq!(result.status.code(), Some(2));
    assert!(result.stdout.is_empty());
    assert!(!String::from_utf8_lossy(&result.stderr).contains("panicked"));
}
