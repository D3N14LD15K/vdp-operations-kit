# security.txt Deployment

1. Serve `/.well-known/security.txt` over HTTPS.
2. Keep `Expires` fresh (≤1 year).
3. Optionally provide an OpenPGP signature and a public key at `/pgp.txt`.
