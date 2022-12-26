period = int(input())
doctors = 7

total_rev_pat_count = 0
total_unreviewed_pat_count = 0

for i in range(1, period + 1):
    patient_count = int(input())
    reviewed_pat_count = 0
    unreviewed_pat_count = 0

    if i % 3 == 0 and total_unreviewed_pat_count > total_rev_pat_count:
        doctors += 1

    if doctors >= patient_count:
        reviewed_pat_count = patient_count
    else:
        unreviewed_pat_count = patient_count - doctors
        reviewed_pat_count = patient_count - unreviewed_pat_count

    total_rev_pat_count += reviewed_pat_count
    total_unreviewed_pat_count += unreviewed_pat_count

print(f"Treated patients: {total_rev_pat_count}.")
print(f"Untreated patients: {total_unreviewed_pat_count}.")
