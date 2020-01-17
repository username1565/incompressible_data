# incompressible_data
Try to compress incompressible data

Lossless compression have a fundamental limit, because N-bits data have space of the values in range [0, 2^N].
If each value can be compressed for (N-k) bits, then space of values will be in range [0, 2^(N-k)],
and not each value from previous range can be recovered from this values.

Methods for [entropy encoding](https://en.wikipedia.org/wiki/Entropy_encoding)
can compress not all input data, and only **COMPRESSIBLE DATA**,
this is data with low Shannon information entropy
and this methods compress compressible data - into the output data,
which have high Shannon information entropy.
As result, output data is **INCOMPRESSIBLE DATA**, and this data can be **Big Data**.

The compression rate is limited by [Shannon's_source_coding_theorem](https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem).

After compress **COMPRESSIBLE DATA** - as result we can get **INCOMPRESSIBLE DATA**.

What's **INCOMPRESSIBLE DATA**?
This is a data with high Shannon information entropy.
This is a binary data, where number of TRUE bits, equals or semi-equals of FALSE bits.
**INCOMPRESSIBLE DATA** can be source data, random data, encrypted data, etc...
**INCOMPRESSIBLE DATA** this is data, where probablity of one bit equal or semi-equal of probablity null bit.

If the number of TRUE bits can be reduced for binary data, where 50% one bits and 50% null bits,
then Shannon information entropy will be reduced, and **incompressible data** can be transformed to **compressible data**.

The following code, can open the way to reversive reduce shannon entropy for any random data.
Need to test this, and play with it.

Maybe this can be programmed to realize recursive compression of any **INCOMPRESSIBLE DATA**,
including *Big Data* of genomes, video/audio, webcam-traffic, even random data, and even encrypted data, etc...
