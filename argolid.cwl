class: CommandLineTool
cwlVersion: v1.2
baseCommand: ["python3", "-m", "container"]
inputs:
  inpDir:
    inputBinding:
      prefix: --inpDir
    type: Directory
  outDir:
    inputBinding:
      prefix: --outDir
    type: Directory
  imageName:
    inputBinding:
      prefix: --name
    type: string 
  filepattern:
    inputBinding:
      prefix: --filepattern
    type: string?
  minDim:
    inputBinding:
      prefix: --minDim
    type: int
  visType:
    inputBinding:
      prefix: --visType
    type: string
  ds:
    inputBinding:
      prefix: --ds
    type: string
outputs:
  outDir:
    outputBinding:
      glob: $(inputs.outDir.basename)
    type: Directory
requirements:
  DockerRequirement:
    dockerPull: polusai/argolid-container:0.1.0
  InitialWorkDirRequirement:
    listing:
    - entry: $(inputs.outDir)
      writable: true
  InlineJavascriptRequirement: {}
