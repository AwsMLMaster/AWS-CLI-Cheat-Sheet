## Get first iterator in Kinesis shard that contains records from trim_horizon

```import boto3

if __name__ == '__main__':


import boto3

if __name__ == '__main__':
    print("Starting Main")
    client = boto3.client("kinesis", region_name="eu-west-1")
    # It is up to you to decide how to configure shards iterator
    shard_iterator = client.get_shard_iterator(
        StreamName="TestStream",
        ShardId="shardId-000000000000",
        ShardIteratorType="TRIM_HORIZON"
    )["ShardIterator"]
    i=0
    while shard_iterator is not None:

        result = client.get_records(ShardIterator=shard_iterator)
        records = result["Records"]
        shard_iterator = result["NextShardIterator"]
        #print("Printring ShardIterator:", shard_iterator)
        print("We are ", i , " iterators far from trim horizon")
        i = i+1
        if len(records) == 0:
            print("iterator was empty")
        else:
            print(len(records),"records found in shard iterator with the following data:")
            for record in records:
                print(record["Data"])
            print("Shard iterator value: ")
            print(shard_iterator)

            print("exiting...")
            break```
