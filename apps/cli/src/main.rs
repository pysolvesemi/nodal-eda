use eda_contracts::PRODUCT;
use std::ffi::OsStr;
use std::io::{self, Write};
use std::process::ExitCode;

const HELP: &str = "Nodal-EDA — FPGA development workflow\n\
\n\
Usage: nodal-eda [--help | --version]\n\
\n\
Options:\n\
  -h, --help       Show this help\n\
  -V, --version    Show the product version\n\
\n\
This bootstrap provides help and version commands.\n";

fn main() -> ExitCode {
    let args: Vec<_> = std::env::args_os().skip(1).collect();
    let output = match args.as_slice() {
        [] => HELP.to_owned(),
        [arg] if arg == OsStr::new("--help") || arg == OsStr::new("-h") => HELP.to_owned(),
        [arg] if arg == OsStr::new("--version") || arg == OsStr::new("-V") => {
            format!("{} {}\n", PRODUCT.name, PRODUCT.version)
        }
        _ => {
            let _ = writeln!(io::stderr(), "error: unsupported arguments; use --help");
            return ExitCode::from(2);
        }
    };
    match io::stdout().write_all(output.as_bytes()) {
        Ok(()) => ExitCode::SUCCESS,
        Err(error) if error.kind() == io::ErrorKind::BrokenPipe => ExitCode::SUCCESS,
        Err(_) => ExitCode::FAILURE,
    }
}
