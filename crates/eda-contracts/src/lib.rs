//! Product identity shared by the first CLI and later product entry points.
//!
//! This is not the versioned project or adapter protocol owned by FND-02.

/// Immutable identity of this product build.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct ProductIdentity {
    pub name: &'static str,
    pub version: &'static str,
}

pub const PRODUCT: ProductIdentity = ProductIdentity {
    name: "nodal-eda",
    version: env!("CARGO_PKG_VERSION"),
};
