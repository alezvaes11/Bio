"""
M14 UF2 Exam (2023-02-27)

Write your name, surname and dni.
"""

name:    str = ''
surname: str = ''
dni:     str = ''

assert name,    'Please write your name'
assert surname, 'Please write your surname'
assert dni,     'Please write your dni'




# Question 1
# - Read the following file:
#   - Option A: SARS-CoV-2 reference: NC_045512.2.genbank
#   - Option B: SARS-CoV-2 variant:   OL466363.1.genbank
# - Print the list of unique authors in the genbank.
# ---------------------------------------------------------------------
def q1(genbank_file: Path) -> list[str]:

    pass



# Question 2
# - Read the following two files
#   - Option A: SARS-CoV-2 reference: NC_045512.2.genbank and fragment 'a.fasta'
#   - Option B: SARS-CoV-2 variant:   OL466363.1.genbank  and fragment 'b.fasta'
# - Investigate if the fragment is similar to something found in the genbank, what it is and why
#   Justify it properly.
# ---------------------------------------------------------------------
def q2(genbank_file: Path, fragment_file: Path) -> None:

    pass



# Question 3
# - Once you have finished Question 2, save the results in a new genbank archive.
# - Fill it with as much information as you can.
#   - Option A: 'a.genbank'
#   - Option B: 'b.genbank'
# ---------------------------------------------------------------------
def q3() -> None:

    pass



# Main
# ---------------------------------------------------------------------
def main():

  q1()
  q2()
  q3()


# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if (this_module == main_module): main()
# ---------------------------------------------------------------------

