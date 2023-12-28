clear s s2
% 设置参数
amplitude = 1;          % 振幅
frequency = 100;          % 频率（每秒周期数）
duration = 1;           % 信号持续时间（秒）
sampling_rate = 1000;   % 采样率（每秒样本数）

% 生成时间向量
t = linspace(0, duration, duration * sampling_rate);

% 创建正弦波数据
sin_wave = amplitude * sin(2 * pi * frequency * t);

% 绘制正弦波
subplot(121)
plot(t, sin_wave);
title('Sinusoidal Wave');
xlabel('Time (seconds)');
ylabel('Amplitude');
[normamp, freqnorm] = findFFT(sin_wave,'-sampFreq',sampling_rate, '-window', 'hann');
subplot(122)
plot(freqnorm,normamp,'b');
sin_wave = single(sin_wave);

[d, h] = crc16(sin_wave);
% 设置串口
s = serialport("COM1",115200,"Timeout",10);
write(s, [single(d), sin_wave], "single")




function [crc, hex] = crc16(packet)
crc = 0;
% crc = hex2dec('FFFF');   % for 0xFFFF version
packet = uint16(packet);
for i = 1:length(packet)
    crc = bitxor( crc, bitshift(packet(i),8) );
    for bit = 1:8
        if bitand( crc, hex2dec('8000') )     % if MSB=1
          crc = bitxor( bitshift(crc,1), hex2dec('1021') );
        else
          crc = bitshift(crc,1);
        end
        crc = bitand( crc, hex2dec('ffff') );  % trim to 16 bits
    end
end
hex = dec2hex(crc);
end