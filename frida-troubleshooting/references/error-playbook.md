# Error Playbook

## Version Mismatch

Symptoms: protocol errors, attach disconnects, unexplained early stream end.

Checks:

```bash
frida --version
frida-ps -Uai
adb shell /data/local/tmp/frida-server --version
```

Align host package and device server/Gadget versions.

## Java Class Not Found

Likely causes: wrong package version, class not loaded yet, custom class loader, obfuscation.

Next checks: enumerate methods with `/isu`, probe class loaders, spawn earlier.

## ObjC Is Not Defined Or Unavailable

Likely causes: not an ObjC process, bridge unavailable due to setup/version issue, attaching too early or to helper process.

Next checks: minimal `ObjC.available` script, process identity, Frida version, rootless jailbreak package compatibility.

## Hook Crashes Target

Likely causes: wrong signature, invalid pointer read, recursive replacement, stale `retval`, string lifetime bug, hot hook overhead.

Next checks: remove mutation, add null/readability guards, log call stack, verify ABI and argument types.

## Hook Never Fires

Likely causes: wrong overload, wrong process, function in another module, late/early timing, target uses native path instead of Java/ObjC.

Next checks: hook caller and callee boundaries, enumerate loaded modules/classes, spawn with early hook, add loader callbacks.
