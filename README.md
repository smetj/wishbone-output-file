              __       __    __
    .--.--.--|__.-----|  |--|  |--.-----.-----.-----.
    |  |  |  |  |__ --|     |  _  |  _  |     |  -__|
    |________|__|_____|__|__|_____|_____|__|__|_____|
                                       version 2.1.2

    Build composable event pipeline servers with minimal effort.


    ====================
    wishbone.output.file
    ====================

    Version: 1.0.0

    Writes events to a file
    -----------------------


        Writes incoming events to a file.  Each line represents an event. Keep in
        mind no rotation of the file is done so data is always appended to the end
        of the file.


        Parameters:

            - selection(str)("@data")
               |  The part of the event to submit externally.
               |  Use an empty string to refer to the complete event.

            - location(str)("./wishbone.out")
               |  The location of the output file.

            - timestamp(bool)(False)
               |  If true prepends each line with a ISO8601 timestamp.


        Queues:

            - inbox
               |  Incoming messages


