FILE(REMOVE_RECURSE
  "CMakeFiles/scan_genlisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/scan_genlisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
