#!/usr/bin/perl
use strict;
use warnings;
use Text::CSV;
use feature 'say';

my $csv_in = Text::CSV->new({ binary => 1, sep_char => ',', auto_diag => 1 });
my $csv_out = Text::CSV->new({ binary => 1, auto_diag => 1 });

open my $file_in, "<:encoding(utf8)", "prompts-grouped-sorted.csv" or die "prompts-grouped-sorted.csv: $!";
open my $file_out, ">:encoding(utf8)", "prompts-grouped-sorted.fixed.csv" or die "prompts-grouped-sorted.fixed.csv: $!";

my $expected_column_count = 3;  # Replace with your expected column count
while (my $row = $csv_in->getline($file_in)) {
    if (@$row != $expected_column_count) {
        warn("Unexpected column count at line " . ($. + 1) . ": expected $expected_column_count, got " . @$row);
    }
    $csv_out->say($file_out, $row);
}

if (! $csv_in->eof) {
    $csv_in->error_diag();
}

close $file_in;
close $file_out;