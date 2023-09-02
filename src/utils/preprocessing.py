def get_dataset_partitions_tf(ds, train_split=0.8, cv_split=0.1, shuffle=True, shuffle_size=1000, seed=12):
    """
    Splits a dataset into training, cross-validation, and test partitions.

    The test dataset is automatically calculated without specifying a test_split in the parameters.

    Args:
        ds: The input dataset to be partitioned (Tesnorflow batch dataset)
        train_split: The proportion of data to be used for training.
        cv_split: The proportion of data to be used for cross-validation.
        shuffle: Whether to shuffle the dataset before partitioning.
        shuffle_size: The number of elements to buffer for shuffling.
        seed:

    Returns:
        train_ds: The dataset partition for training.
        cv_ds: The dataset partition for cross-validation.
        test_ds: The dataset partition for testing.
    """

    if train_split + cv_split >= 1:
        raise ValueError("Incorrect sizes of training and cv splits")

    ds_size = len(ds)

    if shuffle:
        ds = ds.shuffle(shuffle_size, seed=seed)

    # Calculate the number of batches for each partition
    batches_in_training = int(train_split * ds_size)
    batches_in_cv = int(cv_split * ds_size)

    # Create training dataset by taking batches for training_split
    train_ds = ds.take(batches_in_training)

    # Create temporary test dataset by skipping batches used for training
    tmp_test_ds = ds.skip(batches_in_training)

    # Create cross-validation dataset by taking batches from the temporary test dataset
    cv_ds = tmp_test_ds.take(batches_in_cv)

    # Create test dataset by skipping batches used for cross-validation
    test_ds = tmp_test_ds.skip(batches_in_cv)

    return train_ds, cv_ds, test_ds


